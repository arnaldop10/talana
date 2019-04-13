from django.conf.urls import url
from .views import HomeView, UploadPhotoView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^upload/$', UploadPhotoView.as_view(), name='upload'),
]
