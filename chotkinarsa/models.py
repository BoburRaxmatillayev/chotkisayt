from django.db import models

# Create your models here.
class Bot(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to="Bot/")
    link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.link


class Project(models.Model):
    title = models.CharField(max_length=100)  # Long enough for more descriptive titles
    image = models.ImageField(upload_to="project_images/")  # Clearer upload path
    link = models.URLField(max_length=200)  # URLField may be more appropriate

    def __str__(self):
        return self.title  # Use title as a string representation

class Attachment(models.Model):
    class AttachmentType(models.TextChoices):
        PHOTO = "Photo"

    file = models.ImageField('Attachment', upload_to='attachments/')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')
    
    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    description = models.TextField()

    def __str__(self):
        return self.phone_number