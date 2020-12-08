from django.db import models
from django.contrib.auth.models import User

    

class file_upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_file = models.FileField(upload_to='question/problem/',max_length=100,null=True)
    


    def __str__(self):
        return self.user.username
