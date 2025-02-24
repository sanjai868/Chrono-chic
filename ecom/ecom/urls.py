"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views
from django.conf.urls.static import static
from ecom import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',myapp.views.login,name='login'),
    path('regform/',myapp.views.regform,name='regform'),
    path('',myapp.views.home,name='home'),
    path('products/',myapp.views.products,name='products'),
    path('adminhm/',myapp.views.adminhm,name='adminhm'),
    path('addprdct/',myapp.views.addprdct,name='addprdct'),
    path('products/',myapp.views.products,name='products'),
    path('proview/<int:id>/',myapp.views.proview, name='proview'),
    path('cart/',myapp.views.Cart,name='cart'),
    path('viewcart/',myapp.views.viewcart, name='viewcart'),
    path('vieworder/',myapp.views.vieworder,name='vieworder'),
    path('delete/<int:id>/',myapp.views.delete,name='delete'),
    path('cancelord/<int:oid_id>/',myapp.views.cancelord, name='cancelord'),
    ]+ static (settings.STATIC_URL,document_root=settings.STATIC_ROOT)
