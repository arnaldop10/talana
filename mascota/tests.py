# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Usuario, Voto


class UsuarioTestCase(TestCase):
    def setUp(self):
        self.test_user = Usuario(nickname="prueba", pet_name='test pet')
        self.test_user.save()

    def test_user_get_string(self):
        self.assertEquals(str(self.test_user), "test pet")

    def test_get_by_id(self):
        self.assertEquals(Usuario.objects.get(id=1), self.test_user)


class VotoTestCase(TestCase):
    def setUp(self):
        self.test_user = Usuario(nickname="prueba", pet_name='test pet')
        self.test_user.save()
        self.test_vote = Voto(ip='127.0.0.1', photo_pet=self.test_user)
        self.test_vote.save()

    def test_get_by_id(self):
        self.assertEquals(Voto.objects.get(id=1), self.test_vote)

    def test_user_get_string(self):
        self.assertEquals(str(self.test_vote), "127.0.0.1")

    def tearDown(self):
        self.test_vote.delete()
