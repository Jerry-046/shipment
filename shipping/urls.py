from django.urls import path
from shipping import views as shippingview

urlpatterns = [
    path('',shippingview.index,name='shipping-home'),
]
