from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    EDUCATION_LEVEL =(
        ('Diploma','Diploma'),
        ('Bachelors Degree','Bachelors Degree')

    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName  = models.CharField(max_length=100)
    universityName = models.CharField(max_length=300)
    level_of_Education = models.CharField(max_length=200, choices=EDUCATION_LEVEL)
    course_name  = models.CharField(max_length=300)
    introduction_Letter_and_cover_letter  = models.FileField(upload_to="files")


    def __str__(self):
        return f'{self.firstName} - { self.universityName }'