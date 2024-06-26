from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages

# Create your views here.
from reg_app.views import *
from reg_app.forms import *
from reg_app.models import *
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

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




def allproducts(request):
    if request.user:
        products=product.objects.filter(status='approved')
    
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
    return redirect('allproducts')


def change_password(request):
    if request.method=='POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=CustomUser.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('Password changed Successfully')
    return render(request,'change_password.html')


def Edit_profile(request):
    form=profileform()
    user=request.user
    if request.method=='POST':
        form=profileform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Upadte Successfully...</h1>')

    return render(request,'Edit_profile.html',{'form':form})







def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    products=product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category,'products':products})






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


#  <--- Add To Cart --->

def Address(request):
    form= UserAddressForm()
    user=request.user
    if request.method=='POST':
        form= UserAddressForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('checkout')

    return render(request,'Address.html',{'form':form})





def add_to_cart(request, product_id):
    product_instance = product.objects.get(pk=product_id)
  
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product_instance) 


    
    if Wishlist.objects.filter(user=request.user, products=product_instance).exists():
        wishlist_item = Wishlist.objects.get(user=request.user, products=product_instance)
        wishlist_item.delete()

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')

def view_cart(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def removecart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
   
    cart_item.delete()
    return redirect('view_cart')



def checkout(request):
    user_cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})





def update_product_status(request, product_id):
    if request.method == 'POST':
       
        product_obj = product.objects.get(pk=product_id)
        
       
        new_status = request.POST.get('status')
        product_obj.status = new_status
        product_obj.save()
        
       
        return redirect(reverse('category_detail', kwargs={'category_id': product_obj.category_id}))
    else:
       
         return HttpResponse("Method not allowed")
















   
# def ShipingAddress(request):
#     form=ShipingAddressForm()
#     if request.method=='POST':
#         form=ShipingAddressForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('viewaddress')
#     return render(request,'ShipingAddress.html',{'form':form})

# def viewaddress(request):
#     add=Address.objects.all()
#     return render(request,'checkout.html',{'add':add})


