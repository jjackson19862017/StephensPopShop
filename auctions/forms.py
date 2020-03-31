from django import forms
from .models import Auction
from django.forms import widgets

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('product_id', 'bid_number', 'start_date','end_time','status')
        widgets = {'bid_number': forms.HiddenInput(), 'start_date': forms.HiddenInput(),'end_time': forms.HiddenInput(),'status': forms.HiddenInput()}