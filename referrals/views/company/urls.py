from django.urls import path
from . import views

urlpatterns = [
  path('', views.ListCompany.as_view())
]
