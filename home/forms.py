from django import forms

class dateRangeFilter(forms.Form):
    startDate = forms.DateField()
    endDate = forms.DateField()