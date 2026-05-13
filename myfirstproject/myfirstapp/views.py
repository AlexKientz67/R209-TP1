from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import models, forms
from .models import Livre

# Create your views here.
def index(request):
    return render(request, 'myfirstapp/index.html')

def bibliotheque(request):

    livres = Livre.objects.all()

    return render(request, "myfirstapp/bibliotheque.html",{"livres":livres})

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

def update(request, id):
    livre = Livre.objects.get(pk=id)
    lform = LivreForm(instance=livre)
    return render(request, "myfirstapp/update.html",{"livre":livre,"form":lform})

def traitementupdate(request, id):
    lform = forms.LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False)
        Livre.id = id;
        Livre.save()
        return HttpResponseRedirect("/myfirstapp/bibliotheque/")
    else:
        return render(request, "myfirstapp/update.html",{"form":lform})

def delete(request, id):
    print(id)
    models.Livre.objects.filter(id=id).delete()
    return render(request, "myfirstapp/delete.html")