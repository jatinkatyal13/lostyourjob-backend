from django.urls import path

from . import views

urlpatterns = [
  path('', views.ListSeekerView.as_view()),
  path('myProfile/', views.RetrieveProfile.as_view())
]
