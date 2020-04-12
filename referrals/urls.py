from django.urls import path, include

urlpatterns = [
  path('companies/', include('referrals.views.company.urls')),
  path('seekers/', include('referrals.views.seeker.urls'))
]
