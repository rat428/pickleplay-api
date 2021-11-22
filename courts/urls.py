from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from courts import views

urlpatterns = [
    path('courts/', views.CourtList.as_view()),
    path('courts/nearby', views.get_nearest_courts),
    path('courts/generate', views.generate_courts),
    path('courts/<int:pk>/', views.CourtDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
