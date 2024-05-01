from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Produit


# Create your views here.
def accueil(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))

    Produits = Produit.objects.all().filter(disponible=True)
    p = Paginator(Produits, 3)

    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(Produits.num_pages)

    parametre = {
        "all_ajoute":  page_obj

    }

    return render(request,'Produits/Accueil.html',context=parametre)
def Ajouterproduit(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))
    if request.method=='POST':
        form= request.POST
        nom= form.get("nom")
        prix= form.get("prix")
        quantite= form.get("quantite")
        image= request.FILES.getlist("image")[0]
        text= form.get("text")
        ajout_produit= Produit(nom=nom,prix=prix,quantite=quantite,image=image,description=text)
        ajout_produit.save()

        return redirect(reverse('ListeProduit'))


    return render(request,"Produits/Article.html" )
def listeproduit(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))
    Produits = Produit.objects.all().filter(disponible=False)
    p = Paginator(Produits, 10)

    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(Produits.num_pages)
    parametre = {
        "all_ajoute": page_obj

    }

    return render(request,'Produits/ListeProduit.html',context=parametre )
def connexion(request):
    if request.user.is_authenticated:
        return redirect(reverse('Accueil'))

    if request.method=='POST':
        form= request.POST
        username= form.get("username")
        password= form.get("password")

        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(reverse('Accueil'))
        else:
           ...

    return render(request,"Produits/connexion.html")
def deconnexion(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))
    logout(request)
    return redirect(reverse("connexion"))

def supprimer(request, id):
    Produits = Produit.objects.all().filter(id=id).first()
    Produits.delete()
    return redirect(reverse("ListeProduit"))

def modifier(request ,id):
    Produits= Produit.objects.all().filter(id=id).first()
    Produits.disponible= not Produits.disponible
    Produits.save()
    return redirect(reverse("Accueil"))

