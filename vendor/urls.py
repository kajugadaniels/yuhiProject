from django.conf import settings
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)