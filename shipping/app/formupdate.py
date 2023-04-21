from django.forms import ModelForm
from app.models import *

# Create the form class.
class shippingForm(ModelForm):
    class Meta:
        model = detailToship
        fields = '__all__'
class webFormsite(ModelForm):
    class Meta:
        model = decor
        fields = [ 'Website',  'address', 'cphonenum',  'cpdiscri',  'cpkw',  'cpurl',  'cpEmail',  'logo']
        