
from django.shortcuts import render
from .models import Transaction, Purchase, Sales, Adjust

from rest_framework import generics
from .models import Purchase, Sales, Adjust
from .serializers import PurchaseSerializer, SalesSerializer, AdjustSerializer


def stock_position_report(request):
    transactions = Transaction.objects.all()
    purchases = Purchase.objects.all()
    sales = Sales.objects.all()
    adjusts = Adjust.objects.all()

    context = {
        'transactions': transactions,
        'purchases': purchases,
        'sales': sales,
        'adjusts': adjusts,
    }

    return render(request, 'myapp/stock_position_report.html', context)

class PurchaseListCreateView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SalesListCreateView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class AdjustListCreateView(generics.ListCreateAPIView):
    queryset = Adjust.objects.all()
    serializer_class = AdjustSerializer