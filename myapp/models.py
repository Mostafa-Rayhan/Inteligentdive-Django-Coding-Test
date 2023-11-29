from django.db import models

# Create your models here.

class Purchase(models.Model):
    date = models.DateField()
    product_id = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Calculate the total by multiplying quantity and price
    def calculate_total(self):
        return self.quantity * self.price

    total = models.DecimalField(max_digits=10, decimal_places=2, default=calculate_total)

    def __str__(self):
        return f"{self.date} - Product ID: {self.product_id}"


class Sales(models.Model):
    date = models.DateField()
    product_id = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Calculate the total by multiplying quantity and price
    def calculate_total(self):
        return self.quantity * self.price

    total = models.DecimalField(max_digits=10, decimal_places=2, default=calculate_total)

    def __str__(self):
        return f"{self.date} - Product ID: {self.product_id}"
    

class Adjust(models.Model):
    date = models.DateField()
    product_id = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Calculate the total by multiplying quantity and price
    def calculate_total(self):
        return self.quantity * self.price

    total = models.DecimalField(max_digits=10, decimal_places=2, default=calculate_total)

    def __str__(self):
        return f"{self.date} - Product ID: {self.product_id}"
    

class Transaction(models.Model):
    product = models.CharField(max_length=20)
    date = models.DateField()

    # Opening balance fields
    opening_balance_quantity = models.PositiveIntegerField(default=0)
    opening_balance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Transactional balance fields
    transactional_balance_quantity = models.PositiveIntegerField(default=0)
    transactional_balance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Closing balance fields
    closing_balance_quantity = models.PositiveIntegerField(default=0)
    closing_balance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calculate_transactional_balance(self):
        try:
            # Retrieve quantities and prices for purchases, sales, and adjusts
            purchase_quantity = Purchase.objects.filter(product_id=self.product, date=self.date).aggregate(models.Sum('quantity'))['quantity__sum']
            sales_quantity = Sales.objects.filter(product_id=self.product, date=self.date).aggregate(models.Sum('quantity'))['quantity__sum']
            adjust_quantity = Adjust.objects.filter(product_id=self.product, date=self.date).aggregate(models.Sum('quantity'))['quantity__sum']

            purchase_price = Purchase.objects.filter(product_id=self.product, date=self.date).aggregate(models.Sum('total'))['total__sum']
            sales_price = Sales.objects.filter(product_id=self.product, date=self.date).aggregate(models.Sum('total'))['total__sum']
            adjust_price = Adjust.objects.filter(product_id=self.product, date=self.date).aggregate(models.Sum('total'))['total__sum']

            # Calculate transactional balance as purchase * sale - adjust
            transactional_balance_quantity = max(0, purchase_quantity * sales_quantity - adjust_quantity)
            transactional_balance_amount = max(0, purchase_price * sales_price - adjust_price)

            return transactional_balance_quantity, transactional_balance_amount

        except (TypeError, AttributeError):
            return 0, 0

    def save(self, *args, **kwargs):
        # Update transactional balance before saving
        self.transactional_balance_quantity, self.transactional_balance_amount = self.calculate_transactional_balance()

        # Update closing balance based on opening balance and transactional balance
        self.closing_balance_quantity = self.opening_balance_quantity + self.transactional_balance_quantity
        self.closing_balance_amount = self.opening_balance_amount + self.transactional_balance_amount

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - Product: {self.product}"
#model