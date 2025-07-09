from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    Service, SiteContent, Package, ContactMessage,
    SliderItem, SiteDescription, MainCategory,
    Statistic, FooterSection, SocialLink,AboutUs, Technology,Package
)

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title', 'image')

@admin.register(SiteContent)
class SiteContentAdmin(TranslationAdmin):
    list_display = ('about_title', 'email', 'phone')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')

@admin.register(SliderItem)
class SliderItemAdmin(TranslationAdmin):
    list_display = ('title', 'service')

@admin.register(SiteDescription)
class SiteDescriptionAdmin(TranslationAdmin):
    list_display = ('heading',)

@admin.register(MainCategory)
class MainCategoryAdmin(TranslationAdmin):
    list_display = ('title',)

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['label_ar', 'label_en', 'value']

@admin.register(FooterSection)
class FooterSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url')

from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'message', 'created_at']
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')

class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 1

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [TechnologyInline]
