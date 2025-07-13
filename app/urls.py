from django.contrib import admin
from django.urls import path, include
from app.views import home, CustomLoginView, CustomLogoutView




urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('', home, name='home'),

    path('', include('brand.urls')),
    path('', include('category.urls')),
    path('', include('supplier.urls')), 
    path('', include('inflow.urls')),
    path('', include('outflow.urls')),
    path('', include('product.urls')),

    path('api/v1/', include('authentication.urls')), 
        
]
