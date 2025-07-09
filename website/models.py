from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _



class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("العنوان"))
    description = RichTextField(verbose_name=_("الوصف"))
    image = models.ImageField(upload_to='services/',blank=True, null=True, verbose_name=_("صورة الخدمة"))

    def __str__(self):
        return self.title



PACKAGE_CATEGORIES = (
    ('web', 'تصميم وبرمجة المواقع'),
    ('apps', 'تصميم وبرمجة المتاجر والتطبيقات'),
    ('hosting', 'استضافة المواقع والتسويق الإلكتروني'),
)

class SiteContent(models.Model):
    about_title = models.CharField(max_length=200)
    about_description = RichTextField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    footer_text = models.CharField(max_length=255)

    def __str__(self):
        return "إعدادات الموقع"

from django.db import models
from django.utils.translation import gettext_lazy as _

class Package(models.Model):
    CATEGORY_CHOICES = [
        ('web', _('تصميم المواقع')),
        ('app', _('تطبيقات ومواقع')),
        ('hosting', _('الاستضافة والتسويق')),
    ]

      # قائمة ألوان متدرجة للاختيار في لوحة التحكم
    COLOR_CHOICES = [
        ('#f8f9fa', _('رمادي فاتح')),
        ('#e0f7fa', _('أزرق سماوي')),
        ('#ffe0b2', _('برتقالي فاتح')),
        ('#e1bee7', _('بنفسجي فاتح')),
        ('#c8e6c9', _('أخضر فاتح')),
        ('#ffccbc', _('وردي فاتح')),
        ('#d1c4e9', _('بنفسجي رمادي')),
        ('#b2dfdb', _('تركواز فاتح')),
        ('#f0f4c3', _('أصفر زيتوني فاتح')),
    ]

    name = models.CharField(max_length=200, verbose_name=_("عنوان الباقة"))
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name=_("القسم"))
    description = models.TextField(verbose_name=_("وصف الباقة"))
    features = models.TextField(verbose_name=_("مميزات الباقة (افصل كل ميزة بسطر)"))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("السعر الحالي"))
    old_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name=_("السعر قبل الخصم"))
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default="#f8f9fa", verbose_name=_("لون خلفية الباقة"))

    def __str__(self):
        return self.name

    def get_features_list(self):
        return self.features.strip().split('\n')

class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_("Full Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=20, blank=True, verbose_name=_("Phone"))
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Contact Message")
        verbose_name_plural = _("Contact Messages")

    def __str__(self):
        return self.full_name


class SliderItem(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    image = models.ImageField(upload_to='sliders/')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class SiteDescription(models.Model):
    heading = models.CharField(max_length=200)
    description = RichTextField()

    def __str__(self):
        return self.heading

class MainCategory(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.title

from django.db import models

class Statistic(models.Model):
    icon = models.CharField(max_length=100, help_text="FontAwesome class e.g. fa-solid fa-users")
    image = models.ImageField(upload_to='statistics/', null=True, blank=True)
    label_ar = models.CharField(max_length=100, verbose_name="العنوان بالعربية")
    label_en = models.CharField(max_length=100, verbose_name="العنوان بالإنجليزية")
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.label_ar


class FooterSection(models.Model):
    title = models.CharField(max_length=100)
    links = models.TextField(help_text="اكتب كل رابط في سطر جديد بصيغة: النص|الرابط")

    def get_links(self):
        return [line.split("|") for line in self.links.splitlines() if "|" in line]

    def __str__(self):
        return self.title

class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.platform

class AboutUs(models.Model):
    logo = models.ImageField(upload_to='about/', null=True, blank=True)
    company_name = models.CharField(max_length=255)
    heading_ar = models.CharField(max_length=255)
    heading_en = models.CharField(max_length=255)
    description_ar = models.TextField()
    description_en = models.TextField()

    vision_title_ar = models.CharField(max_length=255)
    vision_title_en = models.CharField(max_length=255)
    vision_desc_ar = models.TextField()
    vision_desc_en = models.TextField()

    mission_title_ar = models.CharField(max_length=255)
    mission_title_en = models.CharField(max_length=255)
    mission_desc_ar = models.TextField()
    mission_desc_en = models.TextField()

    goals_title_ar = models.CharField(max_length=255)
    goals_title_en = models.CharField(max_length=255)
    goals_list_ar = models.TextField(help_text=_("افصل كل هدف بسطر جديد"))
    goals_list_en = models.TextField(help_text=_("Separate each goal with a new line"))

    why_us_title_ar = models.CharField(max_length=255)
    why_us_title_en = models.CharField(max_length=255)
    why_us_desc_ar = models.TextField()
    why_us_desc_en = models.TextField()

    techs_title_ar = models.CharField(max_length=255, default="التقنيات التي نعمل بها")
    techs_title_en = models.CharField(max_length=255, default="Technologies We Use")

    def __str__(self):
        return self.company_name


class Technology(models.Model):
    about = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name="technologies")
    image = models.ImageField(upload_to='techs/')
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    desc_ar = models.CharField(max_length=255)
    desc_en = models.CharField(max_length=255)

    def __str__(self):
        return self.name_ar
