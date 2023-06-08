from django.urls import path

from .views import ContactDetailView, AddMessageContact

urlpatterns = [
    path('contact/', ContactDetailView.as_view(), name='contacts'),
    path('contact/add_review/', AddMessageContact.as_view(), name="add_message"),
]
