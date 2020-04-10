from django.urls import path
from auth import views

urlpatterns = [
  path('linkedin/', views.LinkedIn.as_view())
]
