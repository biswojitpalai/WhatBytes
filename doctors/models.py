from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Experience in years")

    def __str__(self):
        return f"{self.name} - {self.specialty}"
