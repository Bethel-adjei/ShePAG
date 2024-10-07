from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


# Model for storing product information
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

# Model for blog posts
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Add image field
    published_date = models.DateTimeField(auto_now_add=True)
    reading_time = models.PositiveIntegerField(default=5)  # Add reading time (in minutes)

    def __str__(self):
        return self.title


# Model for testimonials
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, default="Unknown")  # Default value for existing rows
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)  # Optional field
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.profession} - {self.date.strftime('%Y-%m-%d')}"
#for contact us
class ContactUs(models.Model):
    name=models.CharField(max_length=200, blank=True,null=True)
    email=models.EmailField(blank=True, null=True)
    subject=models.CharField(max_length=500, blank=True, null=True)
    message=models.TextField(max_length=500, blank=True,null=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name="Contact Us"
        verbose_name_plural="Contact Us"

    
    def __str__(self) -> str:
        return f"Message from {self.name} ({self.email})"
    
# this model is for the team members
class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Member')
    message = models.TextField( blank=True, null=True)
    image = models.ImageField(upload_to='teammembers/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)  # Add slug for URL

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(TeamMembers, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

#for newsletter
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

