from django.urls import path, include
from rest_framework import routers
from pizzaass import views

router = routers.DefaultRouter()
router.register(r'Pizza', views.Pizza_RestViewSet)
router.register(r'Customer', views.CustomersViewSet)
router.register(r'All', views.AllViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('pizzaass/', views.pizza_list),
    path('pizzaass/<int:pk>/', views.pizza_detail),
    # path('pizzaass/', views.all_list),
    path('pizzaass/', views.customer_list),
    path('pizzaass/<int:pk>/', views.customer_detail),
    
]
