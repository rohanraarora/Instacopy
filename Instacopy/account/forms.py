from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def __init__(self,*args,**kwargs):
		self.user_cache = None
		super(LoginForm ,self).__init__(*args,**kwargs)

	def clean(self):
		
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
		
			self.user_cache = authenticate(username = username,password = password)
			if self.user_cache is None:
				raise forms.ValidationError("Invalid username password combination")
			elif not self.user_cache.is_active:
				raise forms.ValidationError("Inactive user")
		return self.cleaned_data
	def get_user(self):
		return self.user_cache

		
