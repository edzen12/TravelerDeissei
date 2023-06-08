from django.urls import path
from .views import AboutView


urlpatterns = [
    path('about-us/', AboutView.as_view(), name="about-page"),
]
