from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from .models import Projet,Personnel,Service,Equipe,Detail,Customer,Booking,Avis
from django.http import request
from django.shortcuts import redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

from django.contrib import messages
from .forms import createUserForm,CustomerForm,BookingForm,AvisForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    #template=loader.get_template('magasin/mesProduits.html')
    projets= Projet.objects.all()
    avis=Avis.objects.all()
    context={'projets':projets,'avis':avis,}
    return render(request, "design/mesTraveaux.html",context)

def indexT(request):
    personnels=Personnel.objects.all()
    context={'personnels':personnels}
    return render(request,'design/team.html',context)

def indexP(request):
    return render(request,'design/about.html')
   
def contact(request):
    return render(request,'design/contact.html')

@login_required
def home(request):
    return render(request,'design/accueil.html')
    
def register(request):
    form=createUserForm()
    if request.method == 'POST' :
        form=createUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect('login')


    context={'form':form}
    return render(request,'registration/register.html',context)

def loginPage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user =authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect,check them')
            message={'msg',messages}
            return render(request,'registration/login.html',message)
    context={}
    return render(request,'registration/login.html',context)
def contact(request):
    return render(request,'design/contact.html')

def service(request):
    services=Service.objects.all()
    context={'services':services}
    return render(request,'design/mesServices.html',context)
    
@login_required
def booking(request):
    return render(request,'design/booking.html')

@login_required(login_url='login')
def profile(request):
    projets=request.user.customer.projet_set.all()
    print('PROJETS',projets)
    customer=request.user.customer
    form=CustomerForm(instance=customer)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=customer)
        
        if form.is_valid():
            form.save()

    context={'form':form,'projets':projets}
    return render(request,'design/profile.html',context)


def booking(request):
    submitted = False
    if request.method == "POST":
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('','Your request has been send')
            
    else:
        form = BookingForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "design/booking.html", {'form': form, 'submitted': submitted})

@login_required
def AvisC(request):
    submitted = False
    if request.method == "POST":
        form = AvisForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('','Your Opinion has been send')        
    else:
        form = AvisForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "design/Avis.html", {'form': form, 'submitted': submitted})

    



