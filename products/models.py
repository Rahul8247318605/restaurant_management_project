from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    class Meta:
        verbose_name_plural= "Categories"
    def __str__(self):
        return self.name
class MenuItem(models.Model):
    name=models.CharField(max_length=255,unique=True,help_text="The name of the menu item.")
    description=models.TextField(blank=True, help_text="A short description of the item.")
    price=models.DecimanlField(max_digits=6,decimal_places=2,help_text="The price of the item.")
    class Meta:
        ordering=['name']
        verbose_name="Menu Item"
    def __str__(self):
        return self.name