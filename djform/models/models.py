from django.db import models

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class FormModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    text_field = models.CharField(max_length=5000, blank=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    gender = models.CharField(choices=gender_choices, default='Male', max_length=15)
    address = models.CharField(max_length=255, blank=True, null=True)
    img_file = models.FileField(upload_to='img/', blank=True, null=True)
    video_file = models.FileField(upload_to='video/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
