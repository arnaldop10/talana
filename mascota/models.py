# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Usuario(models.Model):
	nickname = models.CharField(max_length=50)
	pet_name = models.CharField(max_length=100)
	photo_pet = models.FileField(upload_to='photos/')
	votes = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)


class Voto(models.Model):
	ip = models.GenericIPAddressField()
	date = models.DateTimeField(auto_now_add=True)
	photo_pet = models.ForeignKey(Usuario, on_delete=models.CASCADE)
