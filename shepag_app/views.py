from django.shortcuts import render, get_object_or_404
from .models import Product, BlogPost, Testimonial, ContactUs
from django.contrib import messages

# Home page view
def index(request):
    """
    View for the home page, displaying all products and testimonials.
    """
    products = Product.objects.all()  # Fetch all products
    testimonials = Testimonial.objects.all()  # Fetch all testimonials
    
    # Combine both products and testimonials into a single context
    context = {
        'products': products,
        'testimonials': testimonials,
    }

    return render(request, 'index.html', context)  # Render the template with the combined context


# About page view
def about(request):
    """
    View for the 'About Us' page.
    """
    context = {}
    template_page = 'about.html'
    return render(request, template_page, context)

# Product page view
def product(request):
    """
    View for the product page, displaying all products.
    """
    products = Product.objects.all()  
    context = {
        'products': products,
    }
    template_page = 'product.html'
    return render(request, template_page, context)

# Blog page view
def blog(request):
    """
    View for the blog page, displaying all blog posts.
    """
    blog_posts = BlogPost.objects.all()  # Fetch all blog posts
    context = {
        'blog_posts': blog_posts,
    }
    template_page = 'blog.html'
    return render(request, template_page, context)

# Contact page view
def contact(request):
    """
    View for the contact page, handles contact form submissions and displays messages.
    """
    contacts = ContactUs.objects.all()  # Fetch all contact submissions
    if request.method == "POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save the new contact message
        contact_instance = ContactUs(name=name, email=email, phone=phone, message=message)
        contact_instance.save()

        # Display success message
        messages.success(request, "Heya, we received your message, we shall revert")

    context = {
        'contacts': contacts
    }
    template_page = 'contact.html'
    return render(request, template_page, context)

# Team page view
def team(request):
    """
    View for the 'Team' page.
    """
    template_page = 'team.html'
    return render(request, template_page)

# Search Page View
def search(request):
    query = request.GET.get('q')  # Get the search term from the URL
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.none()  # Return no results if query is empty

    context = {
        'products': products,
        'query': query,
    }

    return render(request, 'search.html', context)
# Product detail
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})



# Testimonial page view


def testimonial(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial.html', {'testimonials': testimonials})


# 404 error page view
def error_404(request):
    """
    View for the custom 404 error page.
    """
    context = {}
    template_page = '404.html'
    return render(request, template_page, context)
