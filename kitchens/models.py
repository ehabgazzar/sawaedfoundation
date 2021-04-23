from django.db import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('B', 'Both')
)


# Create your models here.
class Kitchen(models.Model):
    name = models.CharField(max_length=100)
    joining_date = models.DateTimeField('date to join')
    address = models.CharField(max_length=250)
    donation_type = models.CharField(max_length=250)
    admin1_name = models.CharField(max_length=100)
    admin1_phone = models.CharField(max_length=20)
    admin2_name = models.CharField(max_length=100)
    admin2_phone = models.CharField(max_length=20)
    organization_name = models.CharField(max_length=100)
    number_of_cases = models.PositiveBigIntegerField()
    number_of_working_days = models.PositiveBigIntegerField()
    volunteers_type = models.CharField(choices=GENDER_CHOICES, max_length=1)
    number_of_volunteers = models.PositiveBigIntegerField()
