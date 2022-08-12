from django.urls import path

from .views import IndexPageView, SupportBetterplacePageView, BlogNewsPageView, OurTeamPageView, JobsPageView, PressPageView, CategoryPageView, LocationPageView, DonationOverviewPageView, DonationReceiptPageView, RecuringDonationsPageView, GallaryPageView, CeremonialActivitiesPageView, EmailAddressPageView   
urlpatterns= [path('', IndexPageView.as_view(), name='home'),
              path('about/support-betterplace', SupportBetterplacePageView.as_view(), name='support-betterplace'),
              path('about/blog-news', BlogNewsPageView.as_view(), name='blog-news'),
              path('about/our-team', OurTeamPageView.as_view(), name='our-team'),
              path('about/jobs', JobsPageView.as_view(), name='jobs'),
              path('about/press', PressPageView.as_view(), name='press'),
              path('discover/category', CategoryPageView.as_view(), name='category'),
              path('discover/location', LocationPageView.as_view(), name='location'),              
              path('donations/donation-overview', DonationOverviewPageView.as_view(), name='donation-overview'),
              path('donations/donation-receipt', DonationReceiptPageView.as_view(), name='donation-receipt'),
              path('donations/recuring-donations', RecuringDonationsPageView.as_view(), name='recuring-donations'),
              path('events/gallary', GallaryPageView.as_view(), name='gallary'),
              path('events/ceremonial-activities', CeremonialActivitiesPageView.as_view(), name='ceremonial-activities'),
              path('login/email-address', EmailAddressPageView.as_view(), name='email-address'), 
              
             ]
