from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    Service, Package, SiteContent, SliderItem,
    SiteDescription, MainCategory, Statistic, FooterSection, SocialLink, AboutUs
)
from django.contrib import messages
from django.utils.translation import get_language
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext as _
import requests

def home(request):
    services = Service.objects.all()[:8]  # نعرض 8 خدمات على الصفحة الرئيسية
    sliders = SliderItem.objects.all()
    site_description = SiteDescription.objects.first()
    main_categories = MainCategory.objects.all()
    statistics = Statistic.objects.all()
    site_content = SiteContent.objects.first()  # بيانات عامة مثل الفوتر والبريد

    context = {
        'services': services,
        'sliders': sliders,
        'site_description': site_description,
        'main_categories': main_categories,
        'statistics': statistics,
        'site_content': site_content,
        'footer_sections': FooterSection.objects.all(),
        'social_links': SocialLink.objects.all(),
    }
    return render(request, 'website/home.html', context)



def about_view(request):
    about = AboutUs.objects.first()
    techs = about.technologies.all()
    return render(request, 'website/about.html', {
        'about': about,
        'techs': techs,
    })

def test(request):
    site_content = SiteContent.objects.first()
    return render(request, 'website/test.html', {'site_content': site_content})


def services(request):
    services = Service.objects.all()
    site_content = SiteContent.objects.first()
    return render(request, 'website/services.html', {'services': services, 'site_content': site_content})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    services = Service.objects.exclude(pk=pk)  # باقي الخدمات
    social_links = SocialLink.objects.all()

    return render(request, 'website/service_detail.html', {
        'service': service,
        'services': services,
        'social_links': social_links,
    })




def packages_by_category(request, category_slug):
    # category_slug سيكون مثلاً: 'web' أو 'app' أو 'hosting'
    packages = Package.objects.filter(category=category_slug)

    # عنوان وسطرين وصف لكل قسم (تقدر تعدلهم أو تخزنهم في قاعدة بيانات لو حابب)
    titles = {
        'web': 'تصميم المواقع',
        'app': 'تطبيقات ومواقع',
        'hosting': 'الاستضافة والتسويق',
    }
    descriptions = {
        'web': 'صفحة تعرض باقات تصميم المواقع المختلفة مع التفاصيل والأسعار.',
        'app': 'صفحة تعرض باقات التطبيقات والمواقع مع خيارات مميزة تناسب احتياجاتك.',
        'hosting': 'صفحة تعرض باقات الاستضافة والتسويق بأفضل الأسعار والعروض.',
    }

    context = {
        'packages': packages,
        'category_title': titles.get(category_slug, ''),
        'category_description': descriptions.get(category_slug, ''),
    }
    return render(request, 'website/packages_category.html', context)



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # إرسال بريد إلكتروني
            send_mail(
                subject=f"رسالة جديدة من {contact.full_name}",
                message=contact.message,
                from_email=contact.email,
                recipient_list=['your_email@example.com'],
            )

            # إرسال إلى واتساب (API مثل UltraMsg أو Twilio)
            # requests.post('https://api.ultramsg.com/instanceID/messages/send', json={...})

            messages.success(request, "تم إرسال رسالتك بنجاح! سنقوم بالتواصل معك قريبًا.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form})

def category_detail(request, pk):
    from .models import MainCategory, SocialLink

    category = get_object_or_404(MainCategory, pk=pk)
    social_links = SocialLink.objects.all()
    lang = get_language()

    context = {
        'category': category,
        'social_links': social_links,
        'lang': lang,
    }
    return render(request, 'website/category_detail.html', context)
