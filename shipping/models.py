from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural="Countries"
    
    def __str__(self):
        return self.name
    

class Shipment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    sender_country=models.ForeignKey(Country,related_name='sender_country',on_delete=models.CASCADE)
    sender_contactnumber = models.CharField(max_length=20,validators=[RegexValidator(regex=r'^\+977-\d{10}$',message='Phone number must be in the format +977-XXXXXXXXXX (where X is a digit).')])
    sender_city=models.CharField(max_length=100)
    sender_postalcode=models.IntegerField()
    sender_telephone1=models.IntegerField(blank=True,null=True)
    sender_telephone2=models.IntegerField(blank=True,null=True)
    sender_address=models.CharField(max_length=100)
    reciever_country=models.ForeignKey(Country,related_name='reciever_country',on_delete=models.CASCADE)
    reciever_firstname=models.CharField(max_length=100)
    reciever_lastname=models.CharField(max_length=100)
    reciever_contactnumber = models.CharField(max_length=20,validators=[RegexValidator(regex=r'^\+977-\d{10}$',message='Phone number must be in the format +977-XXXXXXXXXX (where X is a digit).')])
    reciever_email=models.EmailField()
    reciever_city=models.CharField(max_length=100)
    reciever_postalcode=models.IntegerField(blank=True,null=True)
    reciever_telephone1=models.IntegerField(blank=True,null=True)
    reciever_telephone2=models.IntegerField(blank=True,null=True)
    reciever_address=models.CharField(max_length=100)

    def __str__(self):
        return f"Shipment from {self.sender_city} to {self.reciever_city}"

    

        
