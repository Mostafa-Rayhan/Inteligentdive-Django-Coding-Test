# myapp/urls.py

from django.urls import path
from .views import stock_position_report
from .views import PurchaseListCreateView, SalesListCreateView, AdjustListCreateView

app_name = 'myapp'

urlpatterns = [
    path('', stock_position_report, name='stock_position_report'),
    # Add other URLs as needed for additional views
    path('purchases/', PurchaseListCreateView.as_view(), name='purchase-list-create'),
    path('sales/', SalesListCreateView.as_view(), name='sales-list-create'),
    path('adjusts/', AdjustListCreateView.as_view(), name='adjust-list-create'),
]
