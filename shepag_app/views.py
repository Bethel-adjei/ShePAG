from django.shortcuts import render

# Create your views here.

# Home page
def index(request):
    return render(request, 'index.html')

# About page
def about(request):
    return render(request, 'about.html')

# Product page
def product(request):
    return render(request, 'product.html')

# Blog page
def blog(request):
    return render(request, 'blog.html')

# Contact page
def contact(request):
    return render(request, 'contact.html')

# Team page
def team(request):
    return render(request, 'team.html')

# Testimonial page
def testimonial(request):
    return render(request, 'testimonial.html')

# 404 error page
def error_404(request, exception):
    return render(request, '404.html')
