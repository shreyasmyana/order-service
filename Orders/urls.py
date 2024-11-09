from django.urls import path

import Orders
from Orders.views import OrderCreateView,serviceHealth

urlpatterns = [
    path('service-health/',serviceHealth, name='orders'),
    path('create_order/', OrderCreateView.as_view(), name='create_order'),

]