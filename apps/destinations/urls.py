from django.urls import path
from .views import DestinationListView


urlpatterns = [
    path("destinations", DestinationListView.as_view(), name="list_destination"),
]
