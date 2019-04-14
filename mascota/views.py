# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View

from .forms import UploadPhotoForm
from .models import Usuario, Voto


class HomeView(View):
    template_name = 'mascota/home.html'

    def get(self, request, *args, **kwargs):
        users = Usuario.objects.all().order_by('-votes')
        data = []
        for user in users:
            data.append({
                'nickname': user.nickname,
                'pet_name': user.pet_name,
                'published': user.created_at,
                'photo_pet': user.photo_pet,
                'photo_id': user.photo_pet.name.split('/')[-1],
                'votes': user.votes
            })

        return render(request, self.template_name, {'pets': data})

    def post(self, request, *args, **kwargs):
        photo_id = request.POST.get('id')
        ip = request.POST.get('ip')

        user = Usuario.objects.get(photo_pet__contains=photo_id)
        user.votes += 1
        user.save()

        voto = Voto()
        voto.ip = ip
        voto.photo_pet = user
        voto.save()

        users = Usuario.objects.all().order_by('-votes')
        data = []
        for user in users:
            data.append({
                'nickname': user.nickname,
                'pet_name': user.pet_name,
                'published': user.created_at,
                'photo_pet': user.photo_pet,
                'photo_id': user.photo_pet.name.split('/')[-1],
                'votes': user.votes
            })

        response = render(request, self.template_name, {'pets': data})
        response.set_cookie('ip', ip)
        return response


class UploadPhotoView(View):
    form_class = UploadPhotoForm
    success_url = reverse_lazy('home')
    template_name = 'mascota/upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})
