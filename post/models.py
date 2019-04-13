from django.db import models

# Create your models here.
from member.models import Xmember
from location_field.models.plain import PlainLocationField



class Party(models.Model):
    organiser = models.ForeignKey(Xmember,on_delete=models.CASCADE,null=True,blank=True, related_name='organiser')
    city = models.CharField(max_length=255)
    title = models.CharField(max_length=150,)
    image = models.ImageField(upload_to='media/party_place')
    description = models.TextField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
    attenders = models.ManyToManyField(Xmember, related_name='attenders')
    date = models.DateTimeField(auto_created=True,null=True)