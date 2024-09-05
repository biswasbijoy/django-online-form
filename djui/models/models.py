from django.db import models

class CustomForm(models.Model):
    name = models.CharField(max_length=100)
    fields = models.JSONField(default=dict)  # Store form fields and types as a JSON object

    def __str__(self):
        return self.name
