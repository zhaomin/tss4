# Copyright (C) 2009 Software Institute, Nanjing University 

from django.db import models

# models that constitutes the core tss platform

class Application(models.Model):
    app_key = models.CharField(max_length=200)
    pub_key = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

# models constructed by ERD diagram of original TSS    

class CourseTemplate(models.Model):
    name=models.CharField(max_length=200)
    number = models.CharField(max_length=100, unique=True)

class ModuleTemplate(models.Model):
    name=models.CharField(max_length=200)
    module=models.OneToOneField(Module)

class Course(models.Model):
    name=models.CharField(max_length=200)
    time=models.TimeField()
    teachers = models.ManyToManyField(Person)
    tas = models.ManyToManyField(Person) # teaching assistants
    students = models.ManyToManyField(Person)

class Module(models.Model):
    name=models.CharField(max_length=200)
    grade=models.IntegerField()
    template = models.ForeignKey(ModuleTemplate)
    compulsory_course = models.ManyToManyField(Course)

class Person(models.Model):
    name=models.CharField(max_length=200)
    mailAccount=models.EmailField()
    grade=models.IntegerField()
    role=models.IntegerField()
    module=models.ForeignKey(Module)
    active_courses = models.ManyToManyField(Course)
    finished_courses = models.ManyToManyField(Course)

