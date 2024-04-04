from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from reg_app.views import *
from reg_app.forms import *
from reg_app.models import *
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

def homepage(request):
   
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
            return HttpResponse('<h1>registration successfully.....</h1>')
        else:
            return HttpResponse('<h1>user alredy exits...</h1>')

    return render (request,'registration.html',d)

def userdashbord(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'username':un}
       # return render(request,'userdashbord.html',d)
        return redirect('productlist')
    return render(request,'userdashbord.html')

def dealerdashbord(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'username':un}
        #return render(request,'dealerdashbord.html',d)
        return redirect('create_product')
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
                return redirect('dealerdashbord')
            elif AUO.user:
                return redirect('userdashbord')
            else:
                return redirect('homepage')
                
    return render(request,'loginpage.html')



@login_required
def logoutpage(request):
    logout(request)
    return render(request,'homepage.html')



def create_product(request):
    form=ProductCreationForm()
    if request.method=='POST':
        dataform=ProductCreationForm(request.POST)
        if dataform.is_valid():
           
            dataform.save()
            return HttpResponse('<h1>create product....</h1>')
    return render(request,'create_product.html',{'form':form})


def productlist(request):
    products =product.objects.all()
    return render(request,'productlist.html',{'products':products})


@ login_required
def updateproduct(request):
   products=UpdateCreationForm()
  
   if request.method == 'POST':
        name=request.POST['pname']
        products=product.objects.get(pname=name)
        form = UpdateCreationForm(request.POST, instance=products)
        if form.is_valid():
            form.save()
            return redirect('productlist')
           
   return render(request,'productupdate.html',{'products':products})




def deleteproduct(request):
    #product = get_object_or_404(product, pk=product_id, dealer=request.user)
    pro=DeleteCreationForm()
    if request.method == 'POST':
        
            name=request.POST['pname']
            products=product.objects.get(pk=name)
            
            product.delete(products)
            return redirect('productlist')
    return render(request, 'deleteproduct.html',{'pro':pro})



def addwishlist(request):
    add=WishlistForm()
    if request.method=='POST':
        addproduct=WishlistForm(request.POST)
        if addproduct.is_valid():
             Wishlistiteam=addproduct.save(commit=False)
             Wishlistiteam.product=product
             Wishlistiteam.save()
             addproduct.save()

           

        return redirect('wishlist')
            #return HttpResponse('<h1> Add Product To WishList... </h1>')
    return render(request,'addwishlist.html',{'add':add})


def wishlist(request):
    products=Wishlist.objects.all()
    return render(request,'displaywishlist.html',{'products':products})