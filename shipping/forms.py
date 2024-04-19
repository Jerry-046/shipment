from django import forms
from .models import Feedback,Shipment

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email','subject','message']


class FromForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['sender_country','sender_contactnumber','sender_city','sender_postalcode','sender_telephone1','sender_telephone2','sender_address']

class ToForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['reciever_country','reciever_firstname','reciever_lastname','reciever_contactnumber','reciever_email','reciever_city','reciever_postalcode','reciever_telephone1','reciever_telephone2','reciever_address']




