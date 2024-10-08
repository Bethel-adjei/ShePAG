from django.contrib import admin
from .models import Product, BlogPost, Testimonial, ContactUs,TeamMembers,Subscriber,Newsletter
from django_summernote.widgets import SummernoteWidget 
from django.db import models 
from django.utils.html import mark_safe
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display name in the list view
    search_fields = ('name', 'description')  # Add search functionality

    formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
            
     } 

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'reading_time', 'display_image')
    search_fields = ('title', 'content')
    list_filter = ('published_date',)

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;" />')
        return "No Image"

    display_image.short_description = 'Image'

    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')  # Display name and date
    search_fields = ('name', 'message')  # Add search functionality

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','message','sent_at')  # Display name, email, and phone
    search_fields = ('name', 'email','')  # Add search functionality
    list_filter = ('email',)  # Add a filter by email


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'message', 'image')  # Fields to display in the list view
    search_fields = ('name', 'role')  # Add search functionality
    list_filter = ('role',)  # Add a filter for the 'role' field
    fields = ('name', 'role', 'message', 'image')  # Explicitly show these fields in the form

    formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
            
     } 
    
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']    


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_at')
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Get all subscribers' email addresses
        subscribers = Subscriber.objects.values_list('email', flat=True)

        # Strip HTML tags from the message (Summernote content)
        plain_message = strip_tags(obj.message)

        # Send the newsletter to all subscribers as plain text
        send_mail(
            subject=obj.subject,
            message=plain_message,  # Plain text message
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=subscribers,
            fail_silently=False,
        )

    formfield_overrides = { 
        models.TextField: {'widget': SummernoteWidget},  
    }

     
# Register the models with their custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Subscriber)
admin.site.register(TeamMembers, TeamMembersAdmin)
admin.site.register(Newsletter, NewsletterAdmin)