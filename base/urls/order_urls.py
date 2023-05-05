
from django.urls import path, include
from base.views import order_views as views

urlpatterns = [
    path('', views.getOrders, name="orders"),
    path('add/', views.addOrderItems, name="add"),
    path('myorders/', views.getMyOrders, name="myorders"),
    path('<str:pk>/', views.getOrderById, name="order-id"),
    path('<str:pk>/pay/', views.updateOrderToPaid, name="order-pay"),
    path('<str:pk>/deliver/', views.updateOrderToDelivered, name="order-deliver"),
]
