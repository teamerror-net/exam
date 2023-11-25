from django.db import models

# Create your models here.
class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'CONTACT'
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.fullname
    
class NewsLetter(models.Model):
    class Meta:
        verbose_name_plural = 'NEWSLETTER'
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.email