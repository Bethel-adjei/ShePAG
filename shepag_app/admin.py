from django.contrib import admin
from .models import (
    Product,
    BlogPost,
    Testimonial,
    ContactUs,
    TeamMembers,
    Subscriber,
    Newsletter,
)
from django_summernote.widgets import SummernoteWidget
from django.db import models
from django.utils.html import mark_safe
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Display name in the list view
    search_fields = ("name", "description")  # Add search functionality

    formfield_overrides = {
        models.TextField: {"widget": SummernoteWidget},
    }


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author","published_date", "reading_time", "display_image",)
    search_fields = ("title", "content")
    list_filter = ("author","published_date",)

    def display_image(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;" />'
            )
        return "No Image"

    display_image.short_description = "Image"

    formfield_overrides = {
        models.TextField: {"widget": SummernoteWidget},
    }


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "date")  # Display name and date
    search_fields = ("name", "message")  # Add search functionality


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "message",
        "sent_at",
        "phone_number"
    )  # Display name, email, and phone
    search_fields = ("name", "email", "")  # Add search functionality
    list_filter = ("email",)  # Add a filter by email


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "role",
        "message",
        "image",
    )  # Fields to display in the list view
    search_fields = ("name", "role")  # Add search functionality
    list_filter = ("role",)  # Add a filter for the 'role' field
    fields = (
        "name",
        "role",
        "message",
        "image",
    )  # Explicitly show these fields in the form

    formfield_overrides = {
        models.TextField: {"widget": SummernoteWidget},
    }


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["email", "subscribed_at"]


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
    )  # Display the 'title' and 'created_at' fields in the admin

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Get all subscribers' email addresses
        subscribers = Subscriber.objects.values_list("email", flat=True)

        # Strip HTML tags from the content (Summernote content)
        plain_message = strip_tags(obj.content)

        # Create the email message object with both plain-text and HTML content
        email = EmailMultiAlternatives(
            subject=obj.title,  # 'title' as the subject
            body=plain_message,  # Plain-text message
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.DEFAULT_FROM_EMAIL],  # Send to your email in "To"
            bcc=subscribers,  # Send using BCC to hide recipients from each other
        )

        # Add HTML content as an alternative to the plain-text message
        email.content_subtype = "html"  # Set the content type to HTML
        email.attach_alternative(
            obj.content, "text/html"
        )  # Attach the HTML version of the content

        # Try sending the email
        try:
            email.send(fail_silently=False)
        except Exception as e:
            # Log the error or handle as needed
            print(f"Error sending newsletter: {e}")

    formfield_overrides = {
        models.TextField: {
            "widget": SummernoteWidget
        },  # Use Summernote widget for text fields
    }


# Register the models with their custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Subscriber)
admin.site.register(TeamMembers, TeamMembersAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
