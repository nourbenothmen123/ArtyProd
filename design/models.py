from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Equipe(models.Model):
    nomequipe=models.CharField(max_length=250)
    def __str__(self):
        return self.nomequipe+" "
       
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
class Projet(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    TYPE_CHOICES=[('oui','oui'),('non','non')]
    libellai=models.CharField(max_length=255)
    description=models.TextField()
    date_debut=models.DateField(null=True, default=date.today)
    date_fin=models.DateField(null=True, default=date.today)
    achevé=models.CharField(max_length=3,choices=TYPE_CHOICES)
    equipe=models.OneToOneField(Equipe,on_delete=models.CASCADE,primary_key=True,default=None,)
    def __str__(self):
        return self.libellai+" "+self.description
class Personnel(models.Model):
    nom=models.CharField(max_length=100)
    fichier_cv=models.ImageField(blank=True)
    fichier_photo=models.FileField(upload_to="pictures/",max_length=250,null=True,default=None)
    lien_linkedIn=models.URLField()
    equipe=models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.nom

class Service(models.Model):
    typeService=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(blank=True)
    def __str__(self):
        return self.typeService
    
class Detail(models.Model):
   fichier=models.FileField(upload_to="pictures/",max_length=250,null=True,default=None)
   service=models.ForeignKey(Service,on_delete=models.CASCADE,null=True)
   projet=models.ForeignKey(Projet,on_delete=models.CASCADE,null=True)

class Avis(models.Model):
    FirstName=models.CharField(max_length=50) #prenom
    LastName=models.CharField(max_length=50) #nom
    image=models.ImageField(blank=True)
    avistxt=models.CharField(max_length=255)

class Booking(models.Model):
    service=models.CharField(max_length=255)
    request=models.CharField(max_length=255)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    date=models.DateField(null=True, default=date.today)
    def __str__(self):
        return self.name+" "+self.service
 



