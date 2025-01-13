from django.db import models
import uuid

# import choices

class BaseModel(models.Model):
    id = models.UUIDField(unique=True,primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Site(BaseModel):
    RECORD_CAPACITY_LOW = 1  # user records between 500-10000
    RECORD_CAPACITY_MEDIUM = 2  # user records between 10000-50000
    RECORD_CAPACITY_HIGH = 3  # user records between 50000-200000

    RECORD_CAPACITY_CHOICES = (
        (RECORD_CAPACITY_LOW, "Low"),
        (RECORD_CAPACITY_MEDIUM, "Medium"),
        (RECORD_CAPACITY_HIGH, "High"),
    )

    name = models.CharField(max_length=100)
    domain = models.URLField()
    url = models.URLField()
    description = models.TextField()
    record_capicity = models.IntegerField(choices=RECORD_CAPACITY_CHOICES)


# you can choose to reuse the User model from django.contrib.auth.models
class UserRecords(BaseModel):
    site = models.ForeignKey(Site,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    dob = models.DateField
    is_active = models.BooleanField(default=True)  # do not count for active records if false


        
class JobType(BaseModel):
    exceution_time = models.IntegerField(help_text='Time in seconds') 
    name = models.CharField(max_length=120,blank=True)

class CustomerType(BaseModel):
    name = models.CharField(max_length=120,blank=True)
    record_volume = models.IntegerField() 


    
    




