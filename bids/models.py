from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from auctions.models import Auction
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.

def empty_bid(value):
    if not Bid.bid_price > int("4"):
        raise ValidationError("You need to enter a bid over 5!")
    
class Bid(models.Model):
    product_id = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    bid_views = models.IntegerField(default=0)
    bid_price = models.DecimalField(null=False, max_digits=4, decimal_places=2, default=0, validators=[empty_bid])
    
    
    def __str__(self):
        return "user_id:" + str(self.user_id) + " " + "product_id:" + str(self.product_id) + " " + str(self.bid_views) + " " + str(self.bid_time) + " " + str(self.bid_price)

