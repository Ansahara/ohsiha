import requests
import pandas as pd

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import generic
from .models import autot
from .forms import indexform
from django.conf import settings

from sqlalchemy import create_engine
from bs4 import BeautifulSoup




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


        vuosimalli = []
        mittarilukema = []
        kayttovoima = []
        vaihteisto = []
        links = []
        hinta = []
        ids = []
        moottori = []
        malli = []

        linkki = 'https://www.nettiauto.com/audi/a3'
        #linkki = "https://www.nettiauto.com/" + merkki + "/" + malli
        response = requests.get(linkki)
        soup = BeautifulSoup(response.content, 'html.parser')



        #haetaan kaikki autoihin liittyvät linkit
        car_containers = soup.find_all('a', class_ = 'childVifUrl tricky_link')
        data_box = soup.find_all('div', class_ = 'data_box')
        infos = soup.find_all('div', class_ = 'vehicle_other_info clearfix_nett')


        #käydään infoboksi läpi ja lisätään tiedot listoihin
        for info in infos:
            lis = info.find_all('li', class_ = 'bold')
            vuosimalli.append(lis[0].text)
            if len(lis) == 2:
                mittarilukema.append(lis[1].text)
            else:
                mittarilukema.append('0')


            lis = info.find_all('li')
            if len(lis) == 4:
                kayttovoima.append(lis[2].text)
                vaihteisto.append(lis[3].text)
            else:
                kayttovoima.append('99999')
                vaihteisto.append('99999')



    #käydään läpi data_boxi
        for data in data_box:
            moottori.append(data.span.text)
            malli.append(data.div.text)

    #käydään auto kerraallaan läpi  linkki ja lisätään tiedot listaan
        for car in car_containers:
            links.append(car.get('href'))
            hinta.append(car.get('data-price'))
            ids.append(car.get('data-id'))


        df = pd.DataFrame({'malli':malli, 'hinta':hinta, 'mittarilukema':mittarilukema,
                   'vuosimalli':vuosimalli, 'kayttovoima':kayttovoima,
                   'moottori':moottori, 'vaihteisto':vaihteisto, 'tunniste':ids})

        #muutetaan hinta numeroksi
        df['hinta'] = pd.to_numeric(df['hinta'])
        df['hinta'] = df['hinta'].fillna(0)

        #muutetaan mittarilukema numeroksi
        df['mittarilukema'] = df['mittarilukema'].str.replace('Ajamaton','0')
        df['mittarilukema'] = df['mittarilukema'].str.replace('km','')
        df['mittarilukema'] = df['mittarilukema'].str.replace(' ','')
        df['mittarilukema'] = pd.to_numeric(df['mittarilukema'])

        #muutetaan moottorin koko numeroksi
        df['moottori'] = df['moottori'].str.replace('(','')
        df['moottori'] = df['moottori'].str.replace(')','')
        df['moottori'] = pd.to_numeric(df['moottori'])

        #user = settings.DATABASES['default']['USER']
        #password = settings.DATABASES['default']['PASSWORD']
        #database_name = settings.DATABASES['default']['NAME']

        #database_url = 'sqlite3://{user}:{password}@localhost:8000/{database_name}'.format(
        #user=user,
        #password=password,
        #database_name=database_name,
        #)

        engine = create_engine('sqlite:///db.sqlite3')

        df.to_sql('autot', con=engine, if_exists='replace')


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
