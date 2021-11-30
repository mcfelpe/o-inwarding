"""inwarding_system URL Configuration

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
from django.urls import path
from . import views

# Insert your urlpattern to access your view
# Note that when you create a template, you should also create your url and views
urlpatterns = [
    path('inw_insert', views.inw_insert, name="inw_insert"),
    path('inw_data_table', views.inw_data_table, name="inw_data_table"),
    path('inw_all_table', views.inw_all_table, name="inw_all_table"),
    path('inw_ind_table', views.inw_ind_table, name="inw_ind_table"),
    path('inw_view/<view_item_id>', views.inw_view, name="inw_view"),
    path('inw_view_delete/<view_delete_item_id>', views.inw_view_delete, name="inw_view_delete"),
    path('inw_edit/<edit_item_id>', views.inw_edit, name="inw_edit"),
    path('inw_delete/<delete_item_id>', views.inw_delete, name="inw_delete"),
    path('inw_hod_app/<hod_item_id>', views.inw_hod_app, name="inw_hod_app"),
    path('inw_fin_app/<fin_item_id>', views.inw_fin_app, name="inw_fin_app"),
    path('', views.auth_login, name="auth_login"),
    path('logout_user', views.logout_user, name="logout_user"),
]
