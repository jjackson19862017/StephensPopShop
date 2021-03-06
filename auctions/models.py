from django.db import models
from products.models import Product
from django.utils import timezone
from datetime import datetime, timedelta
# Create your models here.

class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_number = models.IntegerField(default=1)
    start_date = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True, default=timezone.now()+timedelta(days=7))
    status = models.CharField(max_length=10, blank=False, null=False, default="Open")
    current_price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    current_bidder = models.CharField(max_length=100, blank=False, null=False, default="")

    def __str__(self):
        return  "product_id:" + str(self.product_id)
        
        
    
    
    
   