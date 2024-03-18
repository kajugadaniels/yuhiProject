from django.urls import path
from vendor import views

app_name = 'vendor'

urlpatterns = [
    path('dashboard/', views.dashboard, name = 'dashboard'),
    
    path('profile/<str:username>/', views.profile, name = 'profile'),
    path('profile/edit/<str:vid>', views.profileEdit, name = 'profileEdit'),
    
    path('stock/', views.stockRecord, name = 'stockRecord'),
    path('sell-item/', views.sellItem, name = 'sellItem'),
]