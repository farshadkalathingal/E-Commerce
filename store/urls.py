from django.urls import path
from .views import *

urlpatterns = [
    path('', store, name="Store"),
    path('cart/', cart, name="Cart"),
    path('checkout/', checkout, name="Checkout"),
    path('view/<int:pk>/', detail, name="Detail"),
    path('update_item/', updateItem, name="update_item"),
	path('process_order/', processOrder, name="process_order"),

]
