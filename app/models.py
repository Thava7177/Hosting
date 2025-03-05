from django.db import models
import datetime,os

def get_file_name(request, filename):
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{now_time}_{filename}"
    return os.path.join('uploads/images', new_filename)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=25,null=False)
    password = models.CharField(max_length=100,null=False)
    details = models.CharField(max_length=200,blank=True)
    image =  models.ImageField(upload_to=get_file_name, null=True, blank=True)
