from django.contrib import admin
from .models import Product, BlogPost, Testimonial, ContactUs

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display name in the list view
    search_fields = ('name', 'description')  # Add search functionality

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')  # Display title and published date
    search_fields = ('title', 'content')  # Add search functionality
    list_filter = ('published_date',)  # Add a filter by published date

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')  # Display name and date
    search_fields = ('name', 'message')  # Add search functionality

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')  # Display name, email, and phone
    search_fields = ('name', 'email')  # Add search functionality
    list_filter = ('email',)  # Add a filter by email

# Register the models with their custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
