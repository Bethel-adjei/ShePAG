from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('search/', views.search, name='search'),
    path('404',views.error_404, name='404'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Handling 404 errors
#handler404 = 'shepag_app.views.error_404'
