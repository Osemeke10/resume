from django.forms import ModelForm
from models import Contact

class ContactForm(Model.Form):
	class Meta:
		model = Contact
		fields = '__all__'
