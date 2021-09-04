from django.contrib import admin
from Ecommerce.models import Product , Size_Choice , Order
# # # # Register your models here.

admin.site.register(Size_Choice)

class ChoiceInline(admin.StackedInline):
    model = Size_Choice
    extra = 2

class OrderAdmin(admin.ModelAdmin):
    list_display = ('Email','Item','Pub_Date','City')
    search_fields = ('Email','PhoneNumber','City')
    list_filter = ['Pub_Date']
    fieldsets = [
        (None,               {'fields': ['Item']}),
        (None,               {'fields': ['ItemQty']}),
        (None,               {'fields': ['ItemPrice']}),
        (None,               {'fields': ['Email']}),
        (None,               {'fields': ['PhoneNumber']}),
        (None,               {'fields': ['Address']}),
        (None,               {'fields': ['Address2']}),
        (None,               {'fields': ['Province']}),
        (None,               {'fields': ['City']}),
        (None,               {'fields': ['ZipPortal']}),
        (None,               {'fields': ['Details_On_Email']}),
        ('Date information', {'fields': ['Pub_Date'], 'classes': ['collapse']}),
    ]

admin.site.register(Order,OrderAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Title','id','Stock', 'Pub_Date')
    search_fields = ('id','Title','Description','Sub_Category','Brand')
    list_filter = ['Pub_Date']
    fieldsets = [
        (None,               {'fields': ['Title']}),
        (None,               {'fields': ['Description']}),
        (None,               {'fields': ['Category']}),
        (None,               {'fields': ['Sub_Category']}),
        (None,               {'fields': ['Brand']}),
        (None,               {'fields': ['Price']}),
        (None,               {'fields': ['Picture']}),
        (None,               {'fields': ['Picture2']}),
        (None,               {'fields': ['Picture3']}),
        (None,               {'fields': ['Picture4']}),
        (None,               {'fields': ['Stock']}),
        ('Date information', {'fields': ['Pub_Date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Product, ProductAdmin)