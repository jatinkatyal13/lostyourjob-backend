from django.urls import path

from min_io import views

urlpatterns = [
  path('upload/', views.upload)
]
