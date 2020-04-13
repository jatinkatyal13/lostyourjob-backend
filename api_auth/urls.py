from django.urls import path
from api_auth import views

urlpatterns = [
  path('linkedin/', views.LinkedIn.as_view()),

  path('me/', views.me),
  path('logout/', views.logoutView)
]
