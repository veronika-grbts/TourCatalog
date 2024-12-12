from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about, name='about'),
    path('tour/<int:id>/', views.tour_detail, name='tour_detail'),
    path('create/', views.create, name='create'),
    path('tour_type/<str:tour_type_slug>/', views.tour_type, name='tour_type'),
    path('tour/', views.tour_list, name='all_tours'),
    path('tour/<int:id>/edit/', views.tour_update, name='tour_edit'),
    path('tour/<int:id>/delete/', views.tour_delete, name='tour_delete'),
]
