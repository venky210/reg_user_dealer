from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages

# Create your views here.
from reg_app.views import *
from reg_app.forms import *
from reg_app.models import *
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from django.utils.html import mark_safe


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

# def userdashbord(request):
#     if request.session.get('username'):
#         un=request.session.get('username')
#         d={'username':un}
#        # return render(request,'userdashbord.html',d)
#         return redirect('allproducts')
#     return render(request,'userdashbord.html')

# def dealerdashbord(request):
#     if request.session.get('username'):
#         un=request.session.get('username')
#         d={'username':un}
#         #return render(request,'dealerdashbord.html',d)
#         return redirect('dealerproductlist')
#     return render(request,'dealerdashbord.html')


def loginpage(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        AUO=authenticate(username=un,password=pw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=un
            
            if AUO.dealer:
                return redirect('dealerproductlist')
            elif AUO.user:
                return redirect('allproducts')
            elif AUO.admin:
                return redirect('category_list')
    
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
        dataform=ProductCreationForm(request.POST,request.FILES)
        if dataform.is_valid():
            product=dataform.save(commit=False)
            product.dealer=request.user
            product.save()
           
           
            #return HttpResponse('<h1>create product....</h1>')
            return redirect('dealerproductlist')
    return render(request,'create_product.html',{'form':form})


def dealerproductlist(request): 
    products =product.objects.filter(dealer=request.user)
    return render(request,'dealerproductlist.html',{'products':products})


# def create_product(request):
#     if request.method == 'POST':
#         dataform = ProductCreationForm(request.POST)
#         if dataform.is_valid():
#             product = dataform.save(commit=False)
#             product.dealer = request.user
#             product.save()
#             category_id = request.POST.get('category')  # Get category ID from the form
#             return redirect('dealerproductlist', category_id=category_id)
#     else:
#         form = ProductCreationForm()
#     return render(request, 'create_product.html', {'form': form})

# def dealerproductlist(request, category_id=None):
#     if category_id:
#         category = get_object_or_404(Category, id=category_id)
#         products = product.objects.filter(dealer=request.user, category=category)
#     else:
#         products = product.objects.filter(dealer=request.user)
#     return render(request, 'dealerproductlist.html', {'products': products})


def allproducts(request):
    products=product.objects.all()
    return render(request,'allproducts.html',{'products':products})

def product_search(request):
    query = request.GET.get('query')
    products = product.objects.all()
    if query:
        products = products.filter(pname__icontains=query)
    return render(request, 'product_search.html', {'products': products, 'query': query})





# @ login_required
# def updateproduct(request):
#    products=UpdateCreationForm()
  
#    if request.method == 'POST':
#         name=request.POST['pname']
#         products=product.objects.get(pname=name)
#         form = UpdateCreationForm(request.POST, instance=products)
#         if form.is_valid():
#             form.save()
#             return redirect('dealerproductlist')
           
#    return render(request,'productupdate.html',{'products':products})


def updateproduct(request, product_id):
    Product = get_object_or_404(product, pk=product_id, dealer=request.user)
    if request.method == 'POST':
        form =UpdateCreationForm(request.POST, instance=Product)
        if form.is_valid():
            form.save()
            return redirect('dealerproductlist')
    else:
        form = UpdateCreationForm(instance=Product)
    
    return render(request, 'productupdate.html', {'products': form})





def deleteproduct(request,product_id):
    pro = get_object_or_404(product, pk=product_id,dealer=request.user)
   
    if request.method == 'POST':
        
            pro.delete()
            return redirect('dealerproductlist')
    return render(request, 'deleteproduct.html',{'pro':pro})



def addwishlist(request,product_id):
    products=get_object_or_404(product,pk=product_id)
    existing_wishlist_item = Wishlist.objects.filter(user=request.user, products=products).first()

    if existing_wishlist_item:
       
        return redirect('wishlist')
    if request.method=='POST':
      
       
        addproduct=WishlistForm(request.POST)
        if addproduct.is_valid():
            Wishlistiteam=addproduct.save(commit=False)
            Wishlistiteam.user=request.user
            Wishlistiteam.products=products
            Wishlistiteam.save()
           # addproduct.save()
            

            return redirect('wishlist')
        else:
            form=WishlistForm()
  
            #return HttpResponse('<h1> Add Product To WishList... </h1>')
    return render(request,'addwishlist.html',{'form':form,'products':products })


def wishlist(request):
   wishlist_items=Wishlist.objects.filter(user=request.user)
   return render(request,'displaywishlist.html',{'wishlist_items':wishlist_items})


def removewishlistiteam(request,wishlist_id):
    wishlist_item=get_object_or_404(Wishlist,pk=wishlist_id,user=request.user)
    if request.method == 'POST':
            wishlist_item.delete()
            return redirect('wishlist')    
    return render(request,'removewishlistiteam.html')



def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=CustomUser.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('Password changed Successfully')
    return render(request,'change_password.html')


def profile_edit(request):
    form=profileform()
    user=request.user
    if request.method=='POST':
        form=profileform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Profile Edit Successfully....</h1>')

    return render(request,'profile_edit.html',{'form':form})




def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'category_detail.html', {'category': category})






def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
      
        if form.is_valid():
            form.save()
          
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def category_update(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'add_category.html', {'form': form})

def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})



            #  <--   SORTING PRICE  -->

def lowtohigh(request):
    products = product.objects.order_by('price')
    return render(request, 'sort_by_price.html',{'products':products})

def hightolow(request):
    products = product.objects.order_by('-price')
    return render(request, 'sort_by_price.html',{'products':products})