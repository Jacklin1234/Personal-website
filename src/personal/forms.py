from django import forms
from .models import person

class personForm(forms.ModelForm):
	class Meta:
		model = person
		fields = [
			'firstname',
			'lastname',
			'age',
			'gender'

		]