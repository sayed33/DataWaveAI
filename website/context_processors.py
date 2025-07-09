from .models import SiteContent, SocialLink

def global_context(request):
    site_content = SiteContent.objects.first()
    social_links = SocialLink.objects.all()
    return {
        'site_content': site_content,
        'social_links': social_links,
    }
