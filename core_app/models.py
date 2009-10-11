# Copyright (C) 2009 Software Institute, Nanjing University 

from django.db import models

# models that constitutes the core tss platform

class Application(models.Model):
    app_key = models.CharField(max_length=200)
    pub_key = models.CharField(max_length=200)

    # short name which will be shown in the navigation bar; Unicode is
    # acceptable
    name = models.CharField(max_length=200)

    # base path for thi application; must be unique, in lower-case ASCII
    # and shorter than 12 characters (inclusive)
    unix_name = models.CharField(max_length=12);

    description = models.TextField(max_length=200) # detailed description
    link = models.CharField(max_length=200)

# models constructed by ERD diagram of original TSS    
class Module(models.Model):
    name=models.CharField(max_length=200)
    grade=models.IntegerField()

class Person(models.Model):
    name=models.CharField(max_length=200)
    mailAccount=models.EmailField()
    grade=models.IntegerField()
    role=models.CharField(max_length=100)
    module=models.ForeignKey(Module)
    
class Course(models.Model):
    name=models.CharField(max_length=200)
    time=models.TimeField()
    participants=models.ManyToManyField(Person)
    
class CourseTemplate(models.Model):
    name=models.CharField(max_length=200)
    course=models.OneToOneField(Course)

class ModuleTemplate(models.Model):
    name=models.CharField(max_length=200)
    module=models.OneToOneField(Module)
