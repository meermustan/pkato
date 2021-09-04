from django.contrib import admin
from django.urls import path
from Ecommerce import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "Ecommerce"

urlpatterns = [
    path('',views.home, name="home"),
    path('Products',views.products,name="products"),
    path('ProductView',views.productview,name="productview"),
    path('Cart',views.cart,name="cart"),
    path('AddCart',views.addcart,name="addcart"),
    path('RemoveItem',views.removeItem,name="removeItem"),
    path('Profile',views.profile,name="profile"),
    path('WishList',views.wishlist,name="wishlist"),
    path('AddWishList',views.addwishlist,name="addwishlist"),
    path('OrderedItems',views.ordereditems,name="ordereditems"),
    path('CheckoutOrder',views.checkout,name="checkout"),
    path('Login',views.handleLogin,name='login'),
    path('Signup',views.handleSignup,name='signup'),
    path('Logout',views.handleLogout,name='logout')
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
