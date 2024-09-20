from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404',views.error_404, name='404'),
]

# Handling 404 errors
#handler404 = 'shepag_app.views.error_404'
