
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField


class Profile(models.Model):
    EDUCATION_LEVEL =(
        ('Choose education Level','Choose education Level'),
        ('Diploma','Diploma'),
        ('Bachelors Degree','Bachelors Degree')

    )
    PREFERRED_COMPANY = (
        ('Choose your preferred company','Choose your preferred company'),
        ('Safaricom','Safaricom'),
        ('KPLC','KPLC'),
        ('KenGen','KenGen'),
        ('County Government of Kirinyaga','County Government of Kirinyaga'),
        ('Andela Kenya','Andela Kenya'),
        ('KPA','KPA')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName  = models.CharField(max_length=100)
    universityName = models.CharField(max_length=300)
    level_of_Education = models.CharField(max_length=200, choices=EDUCATION_LEVEL, default='Choose education Level')
    current_year_of_study = models.CharField(max_length= 10, help_text="example..3rd year")
    course_name  = models.CharField(max_length=300)
    preferred_company = models.CharField(max_length= 300,choices = PREFERRED_COMPANY, default= 'Choose your preferred company')
    current_location = models.CharField(max_length=300)
    primary_contact = models.IntegerField(help_text="example..0712...209", null=True, blank=True) 
    expected_starting_date = models.DateField()
    alternative_contact = models.IntegerField(help_text="example..0712...209",null=True, blank=True) 
    School_introduction_Letter = models.FileField(upload_to="files",help_text="The letter must have an official institution stamp.")
    insuarance_cover = models.FileField(upload_to="files")
    Qualified = models.BooleanField()
    attached = models.BooleanField()
    disqualify = models.BooleanField()


    def __str__(self):
        return f'{self.firstName } - { self.universityName }'

   
