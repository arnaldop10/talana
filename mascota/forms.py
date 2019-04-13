from django import forms

class UploadPhotoForm(forms.Form):
	nickname = forms.CharField(max_length=50)
	pet_name = forms.CharField(max_length=100)
	photo_pet = forms.ImageField()