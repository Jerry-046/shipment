from django.urls import path
from shipping import views as shippingview

urlpatterns = [
    path('',shippingview.index,name='shipping-home'),
    path('feedback-create/', shippingview.feedback_create, name='feedback_create'),
    path('<int:pk>/', shippingview.feedback_detail, name='feedback_detail'),
    path('<int:pk>/feedback-update/', shippingview.feedback_update, name='feedback_update'),
    path('<int:pk>/feedback-delete/', shippingview.feedback_delete, name='feedback_delete'),
    path('feedback-list/', shippingview.feedback_list, name='feedback_list'),
    path('from/', shippingview.from_form, name='from_form'),
    path('to/<int:shipment_id>/', shippingview.to_form, name='to_form'),
    path('list-shipment', shippingview.shipment_list, name='shipment_list'),
]
