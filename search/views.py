from django.shortcuts import render
from django.http import HttpResponse
from Ecommerce.models import Product , UserDetails
# Create your views here.
def search(request):
    text = request.GET.get("searchText",default="")
    allProd = Product.objects.all()
    searchTitle = allProd.filter(Title__icontains=text)
    searchDesc = allProd.filter(Description__icontains=text)
    searchCategory = allProd.filter(Category__icontains=text)
    searchSub_Category = allProd.filter(Sub_Category__icontains=text)
    searchBrand = allProd.filter(Brand__icontains=text)
    searches = searchTitle|searchDesc|searchCategory|searchSub_Category|searchBrand
    if request.user.is_authenticated:
        current_user = request.user
        userDetails = UserDetails.objects.filter(User=current_user.id)
        wishlist = userDetails.values("Wish_List")
        cartlist = userDetails.values("Cart")
    else:
        wishlist = UserDetails.objects.none()
        cartlist = UserDetails.objects.none()
    prams = {'allProd':searches,'text':text,'wishlist':wishlist,'cartlist':cartlist}
    return render(request,'search/search.html',prams)