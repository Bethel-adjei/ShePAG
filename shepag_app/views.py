from django.shortcuts import render, get_object_or_404
from .models import Product, BlogPost, Testimonial, ContactUs,TeamMembers
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm
# Home page view
def index(request):
    """
    View for the home page, displaying all products, testimonials, and blogs.
    """
    products = Product.objects.all()  # Fetch all products
    testimonials = Testimonial.objects.all()  # Fetch all testimonials
    blog_posts = BlogPost.objects.all()  # Fetch all blog posts
    
    context = {
        'products': products,
        'testimonials': testimonials,
        'blog_posts': blog_posts,  # Pass blog posts to context
    }
    
    return render(request, 'index.html', context)
 


# About page view
def about(request):
    members = TeamMembers.objects.all()  # Retrieve all team members
    return render(request, 'about.html', {'members': members}) 

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
    posts = BlogPost.objects.all().order_by('-published_date')
    return render(request, 'blog.html', {'blog_posts': posts})


# Blog Detail page view
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_details.html', {'post': post})


# Contact page view
@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save the message to the database
            contact_message = ContactUs(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            contact_message.save()  # Save the message to the database

            # Create the email content
            email_message = f"New message from {name} ({email})\n\nSubject: {subject}\n\nMessage:\n{message}"

            # Send email notification to the admin
            send_mail(
                subject=f'Contact Form Submission: {subject}',
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['joekwams123@gmail.com'],  # Replace with your admin email
            )

            # Add success message and clear form
            messages.success(request, 'Your message has been sent successfully!')

            return render(request, 'contact.html', {'form': ContactForm()})  # Empty form after submission

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


# Team page view
def team(request):
    members = TeamMembers.objects.all()  # Fetch all team members from the database
    return render(request, 'team.html', {'members': members})

# Team Detail View
def team_member_detail(request, id):
    # Fetch the team member by id
    member = get_object_or_404(TeamMembers, id=id)
    return render(request, 'team_details.html', {'member': member})

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
