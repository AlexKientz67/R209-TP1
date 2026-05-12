from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import models

# Create your views here.
def index(request):
    return render(request, 'myfirstapp/index.html')

def bibliotheque(request):
    return render(request, 'myfirstapp/bibliotheque.html')

def ajout(request):
    if request.method == 'POST':
        form = LivreForm(request)
        if form.is_valid():
            Livre = form.save()
            return render(request, "myfirstapp/affiche.html",{"Livre":Livre})
        else:
            return render(request, "myfirstapp/ajout.html",{"form":form})
    else:
        form = LivreForm()
        return render(request, "myfirstapp/ajout.html",{"form":form})

def traitement(request):
    lform=LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request, "myfirstapp/affiche.html",{"Livre":Livre})
    else:
        return render(request, "myfirstapp/ajout.html",{"form":lform})

def read(request, id):
    Livre = models.Livre.objects.get(pk=id)
    return render(request, "myfirstapp/affiche.html",{"Livre":Livre})

def traitementupdate(request, id):
    lform=LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        Livre.id = id;
        Livre.save()
        return HttpResponseRedirect("/myfirstapp/")
    else:
        return render(request, "myfirstapp/update.html",{"form":lform, "id": id})

def delete(request, id):
    models.Livre.objects.filter(id=id).delete()
    return HttpResponseRedirect("/myfirstapp/delete.html")