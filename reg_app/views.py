from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.
from reg_app.views import *
from reg_app.forms import *
from reg_app.models import *
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def homepage(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'username':un}
        return render(request,'homepage.html',d)
    return render(request,'homepage.html')

def Registration(request):
    form=CustomUserCreationForm()
    d={'form':form}
    if request.method=='POST':
        user=CustomUserCreationForm(request.POST)
        if user.is_valid():
            MUDFO=user.save(commit=False)
            pw=user.cleaned_data['password']
            MUDFO.set_password(pw)
            MUDFO.save()
            return HttpResponse('registration successfully.....')
        else:
            return HttpResponse('user alredy exits...')

    return render (request,'registration.html',d)

def userdashbord(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'username':un}
        return render(request,'userdashbord.html',d)
    return render(request,'userdashbord.html')

def dealerdashbord(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'username':un}
        return render(request,'dealerdashbord.html',d)
    return render(request,'dealerdashbord.html')


def loginpage(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        AUO=authenticate(username=un,password=pw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=un
            
            if AUO.dealer:
                return HttpResponseRedirect(reverse('dealerdashbord'))
            elif AUO.user:
                return HttpResponseRedirect(reverse('userdashbord'))
            else:
                return HttpResponseRedirect(reverse('homepage'))
                
    return render(request,'loginpage.html')



@login_required
def logoutpage(request):
    logout(request)
    return render(request,'homepage.html')
