from django.conf.urls import url
from .views import all_auctions, open_auction, add_auctions

urlpatterns = [
    url(r'^$', all_auctions, name="auctions"),
    url(r'open_auction', open_auction, name="open_auction"),
    url(r'add_auctions', add_auctions, name="add_auctions"),
  ]