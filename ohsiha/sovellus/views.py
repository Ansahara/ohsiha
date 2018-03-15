from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import generic
from .models import video


#create your views here

class IndexView(generic.ListView):
    template_name = 'sovellus/index.html'
    context_object_name = 'list'

    def get_queryset(self):
        return video.objects.all()

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
