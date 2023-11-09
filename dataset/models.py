from django.db import models

# class student(models.Model):
#     roll_no = models.DecimalField(max_digits=9,decimal_places=0,null=False,blank=False, primary_key=True)
#     name = models.CharField(max_length=50)
#     photo = models.ImageField(upload_to='/static/students')
#     branch = models.CharField()
#     branch = [
#         ("CSE", "Computer Science and Engineering"),
#         ("EE", "Electrical Engineering"),
#         ("ME", "Mechanical Engineering"),
#         ("CE", "Civil Engineering"),
#         ("MEMS", "Metallurgy Engineering and Materials Science"),
#     ]
import os

def file_path(instance,filename):
    path = "documents/"
    format = 'uploaded-'+filename
    return os.path.join(path,format)

class FileHandler(models.Model):

    file_upload = models.FileField(upload_to=file_path)

    def __str__(self):
        return str(self.file_upload)


