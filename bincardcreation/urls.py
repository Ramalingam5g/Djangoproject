"""bincard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from bincardcreation import views
# from bincardcreation.views import MaterialView


urlpatterns = [
    path('Create_Method',views.Create_Method),
    path('',views.display),
    path('display/',views.display,name="display"),
    # path('add/',views.select_material_name),
    
    # path('edit/<str:id>', views.edit,name="edit"),  
    path('update/<str:id>', views.update),  
    # path('delete/<str:id>', views.delete), 
    path('mat/',views.add_materail_view),
    # path (r'^add/(?P<category_id>[0-9]+)', "core.views.add_materail_view", name='add_materail_view'),
]



