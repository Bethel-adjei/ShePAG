from django.db import models

# Create your models here.


# Model for storing product information
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

# Model for blog posts
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Model for testimonials
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date.strftime('%Y-%m-%d')}"
