from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import generic
from .models import autot
from .forms import indexform




#create your views here

def index(request):
    lista = ['hähää']
    lista_1 = ['hohoo']
    if request.method == 'POST':
        form = indexform(request.POST)
        merkki = form['merkki']
        lista.append(merkki)
        malli = form['malli']
        lista.append(malli)
        context = {'lista':lista}
        return render(request, 'sovellus/index.html', {'form': form})
    else:
        form = indexform()
        context = {'lista':lista_1}
        return render(request, 'sovellus/index.html', {'form':form}, context)


def kirjautuminen(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'sovellus/kirjautuminen.html', {'form': form})

def haku(request):
    if request.method == 'POST':
        merkki = Merkki
        malli = Malli
    return render(request, 'sovellus/kirjautuminen.html', {'form': form})
