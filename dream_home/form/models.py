
from django.db import models

# Create your models here.
class Gender(models.Model):
    gender_type=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.gender_type 


class Married_opt(models.Model):
    married_select=models.CharField(max_length=20,null=True)

    def __str__(self):
        return  self.married_select 

class Education_level(models.Model):
    education_level=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.education_level

class Property(models.Model):
    property=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.property

class Province(models.Model):
    province=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.province

class Job_Type(models.Model):
    job_type=models.CharField(max_length=20,null=True)

    def __str__(self):
        return  self.job_type

class Home_Dream(models.Model):
    First_Name=models.CharField(max_length=20,null=True)
    Last_Name=models.CharField(max_length=20,null=True)
    Phone_Number=models.CharField(max_length=20,null=True)
    Email=models.CharField(max_length=20,null=True)
    Permanent_Address=models.CharField(max_length=20,null=True)
    Mailing_Address=models.CharField(max_length=20,null=True)
    Postal_code=models.CharField(max_length=20,null=True)
    City=models.CharField(max_length=20,null=True)
    Province=models.ForeignKey(Province,on_delete=models.CASCADE)
    Job_type=models.ForeignKey(Job_Type,on_delete=models.CASCADE)
    Gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
    Married=models.ForeignKey(Married_opt,on_delete=models.CASCADE)
    Education=models.ForeignKey(Education_level,on_delete=models.CASCADE)
    Property=models.ForeignKey(Property,on_delete=models.CASCADE)
    Job_type=models.ForeignKey(Job_Type,on_delete=models.CASCADE)

    def __str__(self):
        return self.First_Name + ' ' + self.Email + ' ' + ' ' + self.City









