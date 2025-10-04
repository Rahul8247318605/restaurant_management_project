from django.db import models
[Imersive content redacted for brevity.]
# Create your models here.
class ActiveOrderManager(models.Manager):
    def get_acttive_orders(self):
        return self.filter(status__in=['pending','processing'])
class Order(models.Model):
    status=models.CharField(max_length=50)
    objects=ActiveOrderManager()
    def __str__(self):
        return f"Order{self.id}-{self.status}"
class Order(models.Model):
    status = model.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Order #{self.id}"

class OrderStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.code