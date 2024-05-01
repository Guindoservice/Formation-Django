from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import TodoList


# Create your views here.
def todo_index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))

    all_todo_liste = TodoList.objects.all().filter(effectuer=True)
    p = Paginator(all_todo_liste, 5)

    page_number = request.GET.get('page')

    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(all_todo_liste.num_pages)

    # le dictionaire
    parametre = {
        "all_todo_liste": page_obj
    }
    return render(request,'todo/index.html',context=parametre)
def todo_liste(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))

    all_todo_liste = TodoList.objects.all().filter(effectuer=False)
    p = Paginator(all_todo_liste, 5)

    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page( all_todo_liste.num_pages)

# le dictionaire
    parametre = {
        "all_todo_liste":page_obj
    }
    return render(request,
                  'todo/liste.html',
                  context=parametre
                  )
def todo_ajouter(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))

    # La verification du chams de formulaire
    if request.method=="POST":
        form= request.POST
        nom= form.get("nom")

        # enregistre dans la basedonne
        todoliste = TodoList(nom=nom )
        todoliste.save()

        return redirect(reverse("todo_list"))
    return render(request,'todo/ajouter.html')

# suppression
def todo_suprimer(request, id):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))

    todo= TodoList.objects.all().filter(id=id).first()
    todo.delete()
    return redirect(reverse("todo_list"))
def todo_change_etat(request,id):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))

    todo= TodoList.objects.all().filter(id=id).first()
    todo.effectuer = not todo.effectuer
    todo.save()
    return redirect(reverse("todo_list"))
def connexion(request):
    if request.user.is_authenticated:
        return redirect(reverse('todo_index'))

    if request.method=="POST":
        form = request.POST
        username= form.get("username")
        password= form.get('password')
        print(username)
        print(password)
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(reverse('todo_index'))
        else:
            ...


    return render(request,"todo/connexion.html")
def deconnexion(request):
    if not request.user.is_authenticated:
        return redirect(reverse('connexion'))
    logout(request)
    return redirect(reverse('connexion'))

