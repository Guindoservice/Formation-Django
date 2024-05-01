from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Customer


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))

    return render(request,"gestion/index.html")
def nouvelle_facture(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))

    return render(request,'gestion/nouvelle_facture.html')

def nouvel_client(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))
    if request.method== 'POST':
        form= request.POST
        nom= form.get("nom")
        email= form.get("email")
        tel= form.get("tel")
        adresse= form.get("adresse")
        sexe= form.get("sexe")
        date= form.get("date")
        save_by= form.get()
        enregistre= Customer(nom=nom,email=email,telephone= tel,adresse=adresse,sexe= sexe, creat_date=date,save_by=save_by)
        enregistre.save()
        print(enregistre)


    return render(request,'gestion/nouvel_client.html')

def connexion(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = request.POST
        username = form.get("username")
        password = form.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('index'))
        else:
            ...
    return render(request,'connexion.html')

def deconnexion(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))
    logout(request)
    return redirect(reverse('connexion'))


    return render(request,'connexion.html')

