from django.contrib import admin
from .models import Bot,Project,Attachment,Contact
# Register your models here.

admin.site.register((Bot,Project,Attachment,Contact))