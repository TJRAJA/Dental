from django import forms
from dapp.models import denal,c_denal,email

class denalForm(forms.ModelForm):
	class Meta:
		model = denal
		fields = ['p_name','p_email','p_date','p_time']
		

class contactForm(forms.ModelForm):
	class Meta:
		model = c_denal
		fields = ['c_name','c_email','c_subject','c_message']


class emailForm(forms.ModelForm):
	class Meta:
		model = email
		fields = ['email']
	