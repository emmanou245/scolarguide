from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from guide.models import Personal
from .forms import LoginForm

def log0Guide(request):
    dhb_context = {'title': 'CONNEXION'}

    return render(request, 'authentication-login.html', dhb_context)

def loginGuide(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashbordAdm')
        message = 'Erreur ! (Mot de passe ou login)'
        #'administrator	mbouchebomdaulriche@gmail.com	MBOUCHE	ULRICHE 16a475fs'
        return render(request, 'authentication-login.html', {'message': message, 'title': 'CONNEXION', 'username': username})

    dhb_context = {'title': 'CONNEXION'}
    return render(request, 'authentication-login.html', dhb_context)


def logoutGuide(request):
        logout(request)
        return render(request, 'public/choice_orientation.html')


#def loginGuide(request):
 #   if request.method == "POST":
  #      form = LoginForm(request.POST)
   #     if form.is_valid():
    #        name_pers = form.cleaned_data['Username']
     #       pw_pers = form.cleaned_data['Password']
      #      user = authenticate(username=name_pers, password=pw_pers)
       #     if user is not None:
        #        login(request, user)
         #       return redirect('dashbordAdm')
          #  else:
           #     messages.error(request, 'Echec d\'authentification')
            #    return render(request, 'authentication-login.html', {'form': form})
     #   else:
      #      for field in form.errors:
       #         form[field].field.widget.attrs['class']+= ' is-invalid'
        #    return render(request, 'authentication-login.html', {'form': form})
    #else:
     #   form = LoginForm()
      #  return render(request, 'authentication-login.html', {'form': form})