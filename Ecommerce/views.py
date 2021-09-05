from django.shortcuts import render , redirect 
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from Ecommerce.models import Product , Size_Choice , UserDetails , Order , Intresting_Product
import json
import random

#Create your views here.
def home(request):
    # print(Intresting_Product.objects.all().delete())
    allProd = Product.objects.all()
    for items in allProd:
        prodId = allProd.filter(id=items.id)
        prodChoices = Prod_Choices_Filter(items.id)
        prodId.update(Choices=prodChoices)
    brands = allProd.values("Brand")
    brand = [items['Brand'] for items in brands]
    brand = list(set(brand))
    brand = random.sample(brand,3)
    Totalbrands = []
    for items in brand:
        Prod = allProd.filter(Brand=items)
        Totalbrands.append([Prod])
    intresting_Prod = Product.objects.none()
    if request.user.is_authenticated:
        current_user = request.user
        checkedItems = Intresting_Product.objects.filter(User=current_user.id).values("Product")
        for items in checkedItems:
            Prod = items["Product"]
            Prod = allProd.filter(id=Prod)
            intresting_Prod = intresting_Prod|Prod
        userDetails = UserDetails.objects.filter(User=current_user.id)
        wishlist = userDetails.values("Wish_List")
        cartlist = userDetails.values("Cart")
    else:
        wishlist = UserDetails.objects.none()
        cartlist = UserDetails.objects.none()
    recommendedQuery = []
    for items in intresting_Prod:
        Prod = [[items.Category],[items.Sub_Category]]
        recommendedQuery.append(Prod)
    recommendedProds = Product.objects.none()
    for items in recommendedQuery:
        for item in items[0]:
            Prod = allProd.filter(Category__icontains=item)
            recommendedProds = recommendedProds|Prod
        for item in items[1]:
            Prod = allProd.filter(Sub_Category__icontains=item)
            recommendedProds = recommendedProds|Prod
    recommendedProds = list(recommendedProds)
    if len(recommendedProds) >= 5:
        recommendedProds = random.sample(recommendedProds,5)
    allProd = Product.objects.all().order_by('-Pub_Date')
    prams = {'homeActive':'active','allProd':allProd,'wishlist':wishlist,'cartlist':cartlist,'brands':Totalbrands,"recommendProd":recommendedProds}
    return render(request,'index.html',prams)

def products(request):
    if request.user.is_authenticated:
        current_user = request.user
        userDetails = UserDetails.objects.filter(User=current_user.id)
        wishlist = userDetails.values("Wish_List")
        cartlist = userDetails.values("Cart")
    else:
        wishlist = UserDetails.objects.none()
        cartlist = UserDetails.objects.none()
    allProd = Product.objects.all().order_by('-Pub_Date')
    prams = {'productsActive':'active','allProd':allProd,'wishlist':wishlist,'cartlist':cartlist}
    return render(request, 'Ecommerce/products.html',prams)

def productview(request):
    product = request.GET.get("product")
    allProd = Product.objects.all()
    if request.user.is_authenticated:
        current_user = request.user
        check = Intresting_Product.objects.filter(User=current_user.id,Product=int(product))
        if len(check)==0:
            Intresting_Product.objects.create(User=current_user.id,Product=int(product))
        userDetails = UserDetails.objects.filter(User=current_user.id)
        wishlist = userDetails.values("Wish_List")
        cartlist = userDetails.values("Cart")
    else:
        wishlist = UserDetails.objects.none()
        cartlist = UserDetails.objects.none()
    product = allProd.filter(id=product)
    prams = {'productsActive':'active',"allProd":product,'wishlist':wishlist,'cartlist':cartlist}
    return render(request, 'Ecommerce/productview.html',prams)

def Prod_Choices_Filter(prodId):
    choice = Size_Choice.objects.values()
    filteredProd = choice.filter(Product_id=prodId)
    fitere_items = []
    for items in filteredProd:
        prodChoice = items.get("choice")
        fitere_items.append([prodChoice])
    return fitere_items

def cart(request):
    if request.user.is_authenticated:
        current_user = request.user
        query = Product.objects.none()
        allProd = UserDetails.objects.filter(User=current_user.id).values("Cart")
        for items in allProd:
            itemId = items.get('Cart')
            prod = Product.objects.filter(id=itemId)
            query = prod|query
        userDetails = UserDetails.objects.filter(User=current_user.id)
        wishlist = userDetails.values("Wish_List")
        cartlist = userDetails.values("Cart")
        prams = {'cartActive':'active','allProd':query,'wishlist':wishlist,'cartlsit':cartlist}
        return render(request, 'Ecommerce/cart.html',prams)
    else:
        wishlist = UserDetails.objects.none()
        cartlist = UserDetails.objects.none()
        allProd = Product.objects.all()
        prams = {'cartActive':'active','allProd':allProd,'wishlist':wishlist,'cartlist':cartlist}
        return render(request, 'Ecommerce/cart.html',prams)

def addcart(request):
    product = request.POST.get("product",default="")
    if request.user.is_authenticated:
        current_user = request.user
        itemsCheck = UserDetails.objects.filter(Cart=product,User=current_user.id)
        if len(itemsCheck) != 1:
            UserDetails.objects.create(User=current_user.id,Cart=product)
            details = UserDetails.objects.filter(User=current_user.id)
            response = json.dumps({"status":"success", "details": details,"product":product}, default=str)
            return HttpResponse(response)
        else:
            details = UserDetails.objects.filter(User=current_user.id)
            response = json.dumps({"status":"success", "details": details,"product":product}, default=str)
            return HttpResponse(response)
    else:
        response = json.dumps({"status":"notLogin","product":product} , default=str)
        return HttpResponse(response)

def removeItem(request):
    product = request.POST.get("deleteItem")
    if request.user.is_authenticated:
        current_user = request.user
        totalItems = UserDetails.objects.filter(User=current_user.id)
        itemsCheck = UserDetails.objects.filter(Cart=product,User=current_user.id)
        itemsCheck.delete()
        return redirect("Ecommerce:cart")
    else:
        allProd = Product.objects.all()
        prams = {'cartActive':'active','allProd':allProd}
        return render(request, 'Ecommerce/cart.html',prams)

def profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        username = request.user.get_full_name()
        prams = {'profileActive':'active','username':username}
        return render(request, 'Ecommerce/profile.html',prams)
    else:
        prams = {'profileActive':'active'}
        return render(request, 'Ecommerce/profile.html',prams)

def wishlist(request):
    if request.user.is_authenticated:
        current_user = request.user
        query = Product.objects.none()
        allProd = UserDetails.objects.filter(User=current_user.id).values("Wish_List")
        for items in allProd:
            itemId = items.get('Wish_List')
            prod = Product.objects.filter(id=itemId)
            query = prod|query
        userDetails = UserDetails.objects.filter(User=current_user.id)
        wishlist = userDetails.values("Wish_List")
        cartlist = userDetails.values("Cart")
    else:
        wishlist = UserDetails.objects.none()
        cartlist = UserDetails.objects.none()
        query = Product.objects.all()
    prams = {'profileActive':'active','allProd':query,'wishlist':wishlist,'cartlist':cartlist}
    return render(request, 'Ecommerce/wishlist.html',prams)

def addwishlist(request):
    product = request.POST.get("product")
    if request.user.is_authenticated:
        current_user = request.user
        itemsCheck = UserDetails.objects.filter(Wish_List=product,User=current_user.id)
        if len(itemsCheck) != 1:
            UserDetails.objects.create(User=current_user.id,Wish_List=product)
            details = UserDetails.objects.filter(User=current_user.id)
            response = json.dumps({"status":"success","item":"add" , "details": details,"product":product}, default=str)
            return HttpResponse(response)
        else:
            itemsCheck.delete()
            details = UserDetails.objects.filter(User=current_user.id)
            response = json.dumps({"status":"success","item":"remove", "details": details,"product":product}, default=str)
            return HttpResponse(response)
    else:
        response = json.dumps({"status":"notLogin","product":product}, default=str)
        return HttpResponse(response)


def ordereditems(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        address2 = request.POST.get("address2")
        province = request.POST.get("province")
        city = request.POST.get("city")
        zipportal = request.POST.get("zipportal")
        givedetails = request.POST.get("givedetails")
        items = request.POST.getlist("Item")
        allProd = Product.objects.all()
        if givedetails == "on":
            givedetails = True
        else:
            givedetails = False
        qtyLimitCross = []
        stockNotAvilable = []
        for item in items:
            filteredItem = allProd.filter(id=item)
            ItemQty = request.POST.get(f"Item{item}Qty")
            Item = filteredItem.values("id")
            for detials in filteredItem:
                ItemExist = Order.objects.filter(Email=email).filter(Item = item)
                ExistQty = ItemExist.values("ItemQty")
                stock = detials.Stock
                if len(ItemExist) != 0:
                    if stock != 0 and not stock < int(ItemQty):
                        if (ExistQty.get().get("ItemQty")+int(ItemQty)) > 5:
                            if request.user.is_authenticated:
                                qtyLimitCross = []
                            else:
                                qtyLimitCross.append(int(item))
                        else:
                            filteredItem.update(Stock=((detials.Stock)-int(ItemQty)))
                            ItemExist.update(ItemQty = int(ItemQty)+ExistQty.get().get("ItemQty"))
                            if request.user.is_authenticated:
                                current_user = request.user
                                cartUser = UserDetails.objects.all()
                                cartUser.filter(User=current_user.id,Cart=item).delete()
                    else:
                        if request.user.is_authenticated:
                            stockNotAvilable = []
                        else:
                            stockNotAvilable.append(int(item))
                else:
                    ItemPrice = ((detials.Price)*int(ItemQty))
                    if stock != 0 and not stock < int(ItemQty):
                        Order.objects.create(Item=Item,ItemQty=ItemQty,ItemPrice=ItemPrice,Email=email,PhoneNumber=phone,Address=address,Address2=address2,Province=province,City=city,ZipPortal=zipportal,Details_On_Email=givedetails)
                        filteredItem.update(Stock=((detials.Stock)-int(ItemQty)))
                        if request.user.is_authenticated:
                            current_user = request.user
                            cartUser = UserDetails.objects.all()
                            cartUser.filter(User=current_user.id,Cart=item).delete()
                    else:
                        if request.user.is_authenticated:
                            stockNotAvilable = []
                        else:
                            stockNotAvilable.append(int(item))
        if qtyLimitCross != [] and stockNotAvilable != []:
            messages.info(request, stockNotAvilable)
            messages.info(request, qtyLimitCross)
            messages.error(request, '<strong>Order :</strong> Sorry stock not remaning to fulfil your these items order.')
            messages.error(request, '<strong>Order :</strong> Sorry your these items quantity cross maximum limit of order!')
            return redirect('Ecommerce:cart')
        elif qtyLimitCross != []:
            messages.info(request, qtyLimitCross)
            messages.error(request, '<strong>Order :</strong> Sorry your these items quantity cross maximum limit of order!')
            return redirect('Ecommerce:cart')
        elif stockNotAvilable != []:
            messages.info(request, stockNotAvilable)
            messages.error(request, '<strong>Order :</strong> Sorry stock not remaning to fulfil your these items order.')
            return redirect('Ecommerce:cart')
        else:
            messages.success(request, '<strong>Order :</strong> successful.')
            return redirect('Ecommerce:ordereditems')
    else:
        if request.user.is_authenticated:
            current_user = request.user
            orderedItems = Order.objects.filter(Email=current_user.email).values("Item","ItemQty")
            allProd = Product.objects.all()
            query = Product.objects.none()
            qty = []
            for items in orderedItems:
                item = items.get("Item")
                query = allProd.filter(id=item)|query
                qty.append(items.get("ItemQty"))
            zipList = zip(query,qty)
            prams = {'profileActive':'active','allProd':zipList}
            return render(request, 'Ecommerce/ordereditems.html',prams)
        else:
            messages.error(request, '<strong>Not Login :</strong> We contact you on email.')
            return redirect('Ecommerce:home')

def checkout(request):
    if request.method == 'POST':
        allProd = Product.objects.all()
        items = request.POST.getlist("Item")
        query = Product.objects.none()
        qty = []
        totalPrice = 45
        totalQty = 0
        for item in items:
            itemQty = request.POST.get(f"Item{item}Qty",default=1)
            if itemQty == "":
                Item = allProd.filter(id=item)
                query = Item|query
                qty.append('1')
                totalQty += 1
                for detials in Item:
                    totalPrice = detials.Price+totalPrice
            else:
                Item = allProd.filter(id=item)
                query = Item|query
                qty.append(itemQty)
                totalQty += int(itemQty)
                for detials in Item:
                    totalPrice = ((detials.Price)*int(itemQty))+totalPrice
        zipList = list(zip(query,qty))
        prams = {'cartActive':'active','allProd':zipList,"totalPrice":totalPrice,'totalQuantity':totalQty}
        return render(request, 'Ecommerce/checkout.html',prams)


def handleSignup(request):
    if request.method == 'POST':
        firstName = request.POST.get('first-name')
        lastName = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cPassword = request.POST.get('confirm-password')
        # I choose username as a email because email is also a unique.
        myuser = User.objects.create_user(email,email,password)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myuser.save()
        messages.success(request, '<strong>Signup :</strong>Account is successfully created.')
        return redirect("/")
    return render(request, 'account/signup.html') 

def handleLogin(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        User = authenticate(username=email,password=password)
        if User is not None:
            login(request,User)
            messages.success(request, '<strong>Login :</strong>You are successfully login.')
            return redirect("/")
        else:
            messages.error(request, '<strong>Login :</strong>Your details is not valid,try again.')
            return redirect("/")
    return render(request,'account/login.html')

def handleLogout(request):
    logout(request)
    return redirect('/')