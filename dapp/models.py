from django.db import models


# Create your models here.
class denal(models.Model):
	p_name = models.CharField(max_length=64)
	p_email = models.EmailField(max_length=50)
	p_date = models.DateField()
	p_time = models.TimeField()


class c_denal(models.Model):
	c_name = models.CharField(max_length=64)
	c_email = models.EmailField(max_length=50)
	c_subject = models.CharField(max_length=64)
	c_message = models.CharField(max_length=640)

class email(models.Model):
	email = models.EmailField(max_length=50)