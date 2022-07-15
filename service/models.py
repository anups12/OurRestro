from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name= models.CharField(max_length=100)
    user= models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Dishes(models.Model):
    name = models.CharField(max_length=150)
    description= models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    dish= models.ForeignKey(Dishes, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        total = self.quantity*self.dish.price
        return total

    def Order_total(self):
        cart =self.cart.all()
        total = sum([item.get_total for item in cart])
        return total