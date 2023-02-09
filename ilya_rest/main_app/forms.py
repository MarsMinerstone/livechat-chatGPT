from django.forms import ModelForm, TextInput, DateInput, Select
from .models import *
from django import forms
import datetime


class AdderForm(ModelForm):
	class Meta:
		model = Comment
		fields = ["com"]
		widgets = {"com": TextInput(attrs = {
				'class': 'form-control',
				'placeholder': 'Enter Comment'
			})

		}

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = ["c_dishes", "addition"]
		widgets = {"c_dishes": Select(
			),
		"addition": TextInput(attrs = {
				'class': 'form-control',
				'placeholder': 'addition'
			})

		}