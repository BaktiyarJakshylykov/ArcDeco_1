from django.contrib import admin
from .models import Product, Caregory, Partner, Review


@admin.register(Caregory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created', 'available', 'price', 'amount']
    list_display_links = ['title', 'category', 'id']
    list_filter = ['available', 'created']
    list_editable = ['price', 'available']
    search_fields = ['title', ]


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['place', 'title', ]
    list_display_links = ['place', 'title']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['place', 'name', 'grade', 'created']
    list_display_links = ['place', 'name']
    # autocomplete_fields = ('place', )


# @admin.register(Star)
# class StarAdmin(admin.ModelAdmin):
#     list_display = ['id', 'grade']
#     list_display_links = ['grade']



