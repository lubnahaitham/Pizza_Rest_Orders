from rest_framework import serializers
from .models import Pizza_Rest, Customers, All

class Pizza_RestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza_Rest
        fields = ['sizes_pizzas', 'track_orders', 'desired_pizzas', 'number_pizzas', 'status_customer']
        
    #     def create(self, validated_data):
        
    #     # Create and return a new `Pizza_Rest` instance, given the validated data.
            
    #         return Pizza_Rest.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
        
    #     #  Update and return an existing `Pizza_Rest` instance, given the validated data.
        
    #     instance.sizes_pizzas = validated_data.get('sizes_pizzas', instance.sizes_pizzas)
    #     instance.track_orders = validated_data.get('track_orders', instance.track_orders)
    #     instance.desired_pizzas = validated_data.get('desired_pizzas', instance.desired_pizzas)
    #     instance.number_pizzas = validated_data.get('number_pizzas', instance.number_pizzas)
    #     instance.status_customer = validated_data.get('status_customer', instance.status_customer)
    #     instance.save()
    #     return instance
    
        
class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ['customer_id', 'name', 'phone', 'address']
        
    #     def create(self, validated_data):
            
    #         # Create and return a new `Customers` instance, given the validated data.
            
    #         return Customers.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
        
    #     # Update and return an existing `Customers` instance, given the validated data.
        
    #     instance.customer_id = validated_data.get('customer_id', instance.customer_id)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.save()
    #     return instance


class AllSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = All
        fields = ['customers_info', 'pizza_info']
