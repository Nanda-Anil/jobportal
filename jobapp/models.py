from django.db import models

# Create your models here.

# registration
class regmodel(models.Model):
    company=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=300)
    phone=models.IntegerField()
    password=models.CharField(max_length=10)


# upload vacancies
class uploadmodel(models.Model):
    catchoice=[
        ('type','type'),
        ('fulltime','fulltime'),
        ('parttime','parttime'),
    ]
    choice=[
        ('work','work'),
        ('hybrid','hybrid'),
        ('remote','remote'),
    ]
    choices=[
        ('0-0','0-0'),
        ('0-1','0-1'),
        ('1-2','1-2'),
        ('2-3','2-3'),
        ('3-4','3-4'),
        ('4-5','4-5'),
        ('5-6','5-6'),
        ('6-7','6-7'),
        ('7-8','7-8'),
        ('8-9','8-9'),
        ('9-10','9-10')
    ]
    company=models.CharField(max_length=20)
    email=models.EmailField()
    job=models.CharField(max_length=20)
    jobtype=models.CharField(max_length=20,choices=catchoice)
    worktype=models.CharField(max_length=20,choices=choice)
    experience=models.CharField(max_length=20,choices=choices)
    qualification=models.CharField(max_length=20)

# user profile
class usermodel(models.Model):
    image=models.ImageField(upload_to='jobapp/static')
    name=models.CharField(max_length=20)
    email=models.EmailField()
    resume=models.FileField(upload_to='jobapp/static')
    education=models.CharField(max_length=20)
    experience=models.CharField(max_length=20)
    address=models.CharField(max_length=300)
    phone=models.IntegerField()


# user  vacancy apply model
class userapplymodel(models.Model):
    company=models.CharField(max_length=20)
    job=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    resume=models.FileField(upload_to='jobapp/static')

class wishmodel(models.Model):
    company = models.CharField(max_length=20)
    email = models.EmailField()
    job = models.CharField(max_length=20)
    jobtype = models.CharField(max_length=20)
    worktype = models.CharField(max_length=20)
    experience = models.CharField(max_length=20)
    qualification = models.CharField(max_length=20)
