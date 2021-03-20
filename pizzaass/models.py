from django.db import models

# Create your models here.


class Pizza_Rest(models.Model):
    sizes_of_pizza_choices = (("S", "S"),
                              ("M", "M"),
                              ("L", "L"),
                              ("FamilyPizza", "FamilyPizza"))
    sizes_pizzas = models.CharField(max_length=200, choices=sizes_of_pizza_choices, default="S")
    track_order_choices =(("preparing", "preparing"),
                            ("delivered", "delivered"),
                          ("undelivered", "undelivered"),)
    track_orders = models.CharField(max_length=100, choices=track_order_choices, default="preparing") 
    desired_pizzas = models.CharField(max_length=300)
    number_pizzas = models.IntegerField(null=True)
    status_customer = models.CharField(max_length=40)
    # customer_id = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.status_customer

class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    # orders = models.ForeignKey(Pizza_Rest, on_delete= models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    
    def __int__(self):
        return self.customer_id
      
class All(models.Model):
    customers_info = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    pizza_info = models.ForeignKey(Pizza_Rest, on_delete=models.CASCADE, null=True)


    class Meta:
        ordering = ['customers_info']