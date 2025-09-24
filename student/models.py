from django.db import models
from django.contrib import admin
# Create your models here.
class  StudentDetail(models.Model):
    Name=models.CharField(max_length=250,help_text="Tell Your Name")
    Age=models.IntegerField(help_text="Age should be in range of 18 to 22!")
    DOB=models.DateField(help_text="Enter a Vaild Date.")
    REG_NO=models.IntegerField(help_text="Enter a Vaild Date.")
class StudentDetailAdmin(admin.ModelAdmin):
    list_display=('Name','Age','DOB','REG_NO')