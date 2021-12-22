from django.db import models

# Create your models here.

class Users_Table(models.Model):
	#id = models.IntegerField(unique=True, db_column='ID')
    Id = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    class Meta:
        db_table = "Users_Table"

class Account_Table(models.Model):
	#id = models.IntegerField(unique=True, db_column='ID')
    Id = models.CharField(max_length=50)
    AccountHolderName = models.CharField(max_length=50)
    class Meta:
        db_table = "Account_Table"

class Contact_Table(models.Model):
	#id = models.IntegerField(unique=True, db_column='ID')
    Id = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    class Meta:
        db_table = "Contact_Table"