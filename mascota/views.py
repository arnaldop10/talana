# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import UploadPhotoForm


class HomeView(TemplateView):
	template_name = 'mascota/home.html'


class UploadPhotoView(TemplateView):
	template_name = 'mascota/upload.html'
	form_class = UploadPhotoForm

	def get(self, request, *args, **kwargs):
		form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
    	form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('home')

        return render(request, self.template_name, {'form': form})