# Ex02 Django ORM Web Application
## Date: 18.09.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
models.py

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

admin.py
from django.contrib import admin
from.models import StudentDetail,StudentDetailAdmin
# Register your models here.
admin.site.register(StudentDetail,StudentDetailAdmin)


```
## OUTPUT
![alt text](<Screenshot 2025-09-24 091023.png>) ![alt text](<Screenshot 2025-09-24 091004.png>)

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
