from django.urls import path

from . import views

urlpatterns = [
  path('myProfile/', views.RetrieveProfile.as_view())
]
