from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from main.models import Category, Product, File, Contact, Partner, Blog
from main.models.about import About


# INLINE
class FileInline(admin.TabularInline):
    model = File
    fields = ('file',)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'parent_id')


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'price', 'category_id')

    inlines = (FileInline,)


@admin.register(Contact)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('id', 'text')