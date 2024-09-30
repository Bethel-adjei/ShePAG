from django.db import models
from django.contrib.auth.models import User

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
    published_date = models.DateTimeField(auto_now_add=True)
    


    # class Meta:
    #     ordering = ['-created_on']
    #     verbose_name_plural = "Post"


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




class ContactUs(models.Model):
    name=models.CharField(max_length=200, blank=True,null=True)
    email=models.EmailField(blank=True, null=True)
    phone=models.IntegerField()
    message=models.TextField(max_length=500, blank=True,null=True)

    class Meta:

        verbose_name="Contact Us"
        verbose_name_plural="Contact Us"

    
    def __str__(self) -> str:
        return self.name