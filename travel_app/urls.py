from django.urls import path
from .views import KlassAPIView, MehmonxonaAPIView, TravelAPIView

urlpatterns = [
    path('klass/', KlassAPIView.as_view(), name='klass'),
    path('mehmonxona/', MehmonxonaAPIView.as_view(), name='mehmonxona'),
    path('travel/', TravelAPIView.as_view(), name='travel'),
]
