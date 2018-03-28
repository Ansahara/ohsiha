from django import forms

class indexform(forms.Form):
    merkki = forms.CharField(label='Merkki:', max_length=100)
    malli = forms.CharField(label='Malli:', max_length=100)
