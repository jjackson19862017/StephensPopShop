from django.conf.urls import url
from .views import all_bids, bid_on_auction

urlpatterns = [
    url(r'', all_bids, name="bid"),
    url(r'bidon', bid_on_auction, name="bid_on_auction"),
    ]