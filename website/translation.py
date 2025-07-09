from modeltranslation.translator import register, TranslationOptions
from .models import (
    Service, SiteContent, Package, SliderItem,
    SiteDescription, MainCategory
)

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(SiteContent)
class SiteContentTranslationOptions(TranslationOptions):
    fields = ('about_title', 'about_description', 'address', 'footer_text',)

@register(Package)
class PackageTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'features')

@register(SliderItem)
class SliderItemTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle',)

@register(SiteDescription)
class SiteDescriptionTranslationOptions(TranslationOptions):
    fields = ('heading', 'description',)

@register(MainCategory)
class MainCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
