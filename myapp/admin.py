
from django.contrib import admin
from .models import Transaction, Purchase, Sales, Adjust
from .models import Purchase, Sales, Adjust

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'product', 'opening_balance_quantity', 'opening_balance_amount', 'transactional_balance_quantity', 'transactional_balance_amount', 'closing_balance_quantity', 'closing_balance_amount')
    search_fields = ['date', 'product']

# @admin.register(Purchase)
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('date', 'product_id', 'quantity', 'price', 'total')
#     search_fields = ['date', 'product_id']

# @admin.register(Sales)
# class SalesAdmin(admin.ModelAdmin):
#     list_display = ('date', 'product_id', 'quantity', 'price', 'total')
#     search_fields = ['date', 'product_id']

# @admin.register(Adjust)
# class AdjustAdmin(admin.ModelAdmin):
#     list_display = ('date', 'product_id', 'quantity', 'price', 'total')
#     search_fields = ['date', 'product_id']

admin.site.register(Purchase)
admin.site.register(Sales)
admin.site.register(Adjust)