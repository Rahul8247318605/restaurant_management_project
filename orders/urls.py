from django.urls import path
from .views import CouponsValidationView

urlpatterns = [
    path('validate/',CouponsValidationView.as_view(),name='coupons_validate'),
]