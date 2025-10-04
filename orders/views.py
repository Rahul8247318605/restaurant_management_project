from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers  import OrderSerializer
from rest_framework.views import ListAPIView
from rest_framework.response import response
from rest_framework import status
from .models import Coupon
from datetime import datetime
class CouponValidationView(APIView):
    def post(self,request,*args,**kwargs):
        coupon_code=request.data.get('code',None)
        if not coupon_code:
            return Response(
                {"error":"Coupon code is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            coupon=Coupon.objects.get(code=coupon_code)
        except Coupon.DoesNotExist:
            return Response(
                {"error":"Invalid coupon code"},
                status=status.HTTP_404_NOT_FOUND
            )
        today=date.today()
        if not coupon.is_active or not (coupon.valid_from <=today<=coupon.valid_until):
            return Response(
                {"error":"Coupon is no longer valid"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {
                "success":"Coupon is valid.",
                "discount_percentage":coupon.discount_percentage
            },
            status=status.HTTP_200_OK
        )
# Create your views here.
class OrderHistoryView(generics.ListAPIView):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        return Order.objects.filter(user=user)