from functools import partial
from django import forms
from models import Scope

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())
     
class ScopeForm(forms.ModelForm):
     
    class Meta:
        model = Scope
        fields = ('temp_min', 'temp_max', 'hum_min', 'hum_max','sensor') 