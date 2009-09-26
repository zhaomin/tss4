# Copyright (C) 2009 Software Institute, Nanjing University 

from django.db import models

# models that constitutes the core tss platform

class Application(models.Model):
    app_key = models.charField(max_length=200)
    pub_key = models.charField(max_length=200)
    name = models.charField(max_length=200)

