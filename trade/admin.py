from django.contrib import admin
from trade.models import Category, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = (
        'name', 'pub_date', 'edit_date'
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('message',)
    list_display = (
        'message', 'pub_date', 'edit_date'
    )
