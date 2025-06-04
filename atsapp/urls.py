# atsapp/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),  # example view
    path('profile_photo',views.profile_photo,name='profile_photo'),
    path('resume_view',views.resume_view,name="resume_view"),
    path('edit_view',views.edit_view,name="edit_view"),
]
