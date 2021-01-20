from django.db import models

# Create your models here.

class ProductModel(models.Model):
    product_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.product_name

class PurchaseModel(models.Model):
    product_name=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    buying_price=models.IntegerField()
    selling_price=models.IntegerField()
    date=models.DateField(auto_now=True)

class SalesModel(models.Model):
    bill_number=models.IntegerField(unique=True)
    customer_name=models.CharField(max_length=120)
    phone=models.IntegerField()
    bill_total=models.IntegerField()

    def __str__(self):
        return self.bill_number

class OrderModel(models.Model):
    bill_number=models.ForeignKey(SalesModel,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=120)
    quantity=models.IntegerField()
    price=models.Integerfield()


    
            

