from django.db import models

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class FormModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    gender = models.CharField(choices=gender_choices, default='Male', max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
