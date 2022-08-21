
from django.contrib import admin
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),

    path('product/',productAPI.as_view() ),                        #rout for product api
    path('register/',RegisterAPI.as_view() ),                      #rout for register api

    path('index/', views.index, name='index'),
    path('check_out/', views.check_out, name='check_out'),
    path('blog/', views.blog, name='blog'),
    path('shop/', views.shop, name='shop'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('product_page/', views.product_page, name='product_page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]
