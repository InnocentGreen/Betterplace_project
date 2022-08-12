from django.shortcuts import render

from django.views.generic import TemplateView
class IndexPageView(TemplateView):
     template_name= 'home.html'

class SupportBetterplacePageView(TemplateView):
     template_name= 'about/support-betterplace.html'

class BlogNewsPageView(TemplateView):
     template_name= 'about/blog-news.html'

class OurTeamPageView(TemplateView):
     template_name= 'about/our-team.html'

class JobsPageView(TemplateView):
     template_name= 'about/jobs.html'

class PressPageView(TemplateView):
     template_name= 'about/press.html'

class CategoryPageView(TemplateView):
     template_name= 'discover/category.html'

class LocationPageView(TemplateView):
     template_name= 'discover/location.html'

class DonationOverviewPageView(TemplateView):
     template_name= 'donations/donation-overview.html'

class DonationReceiptPageView(TemplateView):
     template_name= 'donations/donation-receipt.html'

class RecuringDonationsPageView(TemplateView):
     template_name= 'donations/recuring-donations.html'

class GallaryPageView(TemplateView):
     template_name= 'events/gallary.html'

class CeremonialActivitiesPageView(TemplateView):
     template_name= 'events/ceremonial-activities.html'

class EmailAddressPageView(TemplateView):
     template_name= 'login/email-address.html'




