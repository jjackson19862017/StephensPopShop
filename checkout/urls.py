from django.conf.urls import url
from .views import checkout, bid_checkout

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^bid/$', bid_checkout, name='bid_checkout'),

]
