from django.urls import path
from rest_framework import routers

from .views import (PackageDetailVew, PackageListView, PackageNoPromoListView,
                    PackageViewSet, package_list)

router = routers.DefaultRouter()
router.register('heroes', PackageViewSet)

urlpatterns = [
    path('packages/', package_list, name="list_packages"),
    path('packages-promo/', PackageListView.as_view(), name="package-promo"),
    path('packages/<str:slug>', PackageDetailVew.as_view(), name="package_detail"),
    path('tour_package/', PackageNoPromoListView.as_view(), name="no_promo_package"),
]
