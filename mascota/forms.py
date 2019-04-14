from django import forms
from .models import Usuario

class UploadPhotoForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('nickname', 'pet_name', 'photo_pet')
		labels = {
			'nickname': 'Nombre de Usuario',
			'pet_name': 'Nombre de Mascota',
			'photo_pet': 'Foto de la Mascota',
		}
		widgets = {
			'nickname': forms.TextInput(attrs={'class': 'form-control'}),
			'pet_name': forms.TextInput(attrs={'class': 'form-control'}),
			'photo_pet': forms.FileInput(attrs={'class': 'form-control'}),
		}
