from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def packages(request):
    return render(request, 'packages.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')


def destination_view(request):
    return render(request, 'destination.html')

def explore_tour_view(request):
    return render(request, 'tour.html')

def travel_booking_view(request):
    return render(request, 'booking.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def travel_guides_view(request):
    return render(request, 'guides.html')

def testimonial_view(request):
    return render(request, 'testimonial.html')

def page_not_found_view(request, exception=None):
    return render(request, '404.html')

