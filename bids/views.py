from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.models import User
from .models import Bid
from auctions.models import Auction
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import messages
from products.models import Product

def all_bids(request):
    """ Shows logged in users all the bids """
    if request.user.is_authenticated:
        bid = Bid.objects.all()
        end_time_list = []
        for i in bid:
            end_time_list.append(str(i.auction_id.end_time))
        return render(request, "bid.html", {"bid": bid, 'end_time':end_time_list})
    else:
        messages.error(request, "You must be Logged in")
        return redirect(reverse('login'))
    return render(request, "bid.html", {"bid": bid})

def bid_on_auction(request):
    
    """ Allows a registered user to bid on open auctions """
    
    if request.method == "POST":
            product_id = request.POST['product_id']
            auction = Auction.objects.get(product_id=product_id)
            """ Make sure Auction is still Open """
            if timezone.now() >= auction.start_time and timezone.now() < auction.end_time:
                product = Product.objects.get(id=product_id)
                current_bid = Bid.objects.filter(product_id=product_id)
                if current_bid:
                    bid = current_bid[0]
                    bid.user_id = request.user
                    bid.bid_time = timezone.now()
                    bid.bid_views += 1
                    bid.bid_price += int(request.POST['UpBid'])
                    bid.save()
                    auction.bid_number += 1
                    auction.save()
                else:
                    new_bid = Bid()
                    new_bid.product_id = product
                    new_bid.auction_id = auction
                    new_bid.user_id = request.user
                    new_bid.bid_time = timezone.now()
                    new_bid.bid_views += 1
                    new_bid.bid_price += int(request.POST['UpBid'])
                    new_bid.save()
                    auction.bid_number += 1
                    auction.save()
                messages.error(request, "Well done you have placed a bid.")
            else:
                auction.status = "Closed"
                auction.save()
                messages.error(request, "This Auction is closed.")
            
    return redirect(reverse('auctions'))