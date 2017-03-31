from django import forms

class LibSearchForm(forms.Form):
	query = forms.CharField()
