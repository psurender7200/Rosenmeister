from django.db import models

class Details(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    created = models.DateField(null=False, blank=False, auto_now=True)

class LettersDigits(models.Model):
    class Meta:
        managed = False
    value = models.TextField(null=True, default=None,)
    created = models.DateTimeField(auto_now_add=True)
