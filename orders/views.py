from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers  import OrderSerializer
# Create your views here.
class OrderHistoryView(generics.ListAPIView):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        return Order.objects.filter(user=user)