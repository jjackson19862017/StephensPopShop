from django import forms
from .models import Auction
from django.forms import widgets

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('product_id', 'bid_number', 'start_date','end_time','status')
        widgets = {'bid_number': forms.HiddenInput(), 'start_date': forms.HiddenInput(),'end_time': forms.HiddenInput(),'status': forms.HiddenInput()}

    def clean_product_id(self, *args, **kwargs):
        product_id = self.cleaned_data.get("product_id")
        if Auction.objects.filter(product_id=product_id):
            raise forms.ValidationError(u'There is an Auction already started for this product.  Please Closed the previous Auction before Starting a new one.')
        return product_id
