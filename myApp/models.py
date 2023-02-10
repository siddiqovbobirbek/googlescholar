from django.contrib.auth.models import User
from django.db import models
from Users.models import CustomUser
import os
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


def file_path(instance, filename):
    path = "documents/"
    format = "uploaded-" + filename
    return os.path.join(path, format)

# Create your models here.
class FileHandler(models.Model):

    file_upload = models.FileField(upload_to=file_path)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    upload_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.file_upload.name)

    def get_file_name(self):
        print("File name is ", self.file_upload.name)
        return str(self.file_upload.name).replace('documents/uploaded-', '')

