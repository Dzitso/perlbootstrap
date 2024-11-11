from django.urls import path
from boootstrapapp import views

urlpatterns=[
   path('',views.index,name='index'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('blog/',views.blog,name='blog'),
   path('services/',views.services,name='services'),
   path('packages/',views.packages,name='packages'),
   path('destination/', views.destination_view, name='destination'),
   path('tour/', views.explore_tour_view, name='explore_tour'),
   path('booking/', views.travel_booking_view, name='travel_booking'),
   path('gallery/', views.gallery_view, name='gallery'),
   path('guides/', views.travel_guides_view, name='travel_guides'),
   path('testimonial/', views.testimonial_view, name='testimonial'),
   path('404/', views.page_not_found_view, name='404'),
]