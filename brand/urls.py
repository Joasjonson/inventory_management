from django.urls import path
from brand.views import BrandListView, BrandCreateView, BrandDetailView, BrandUpdateView, BrandDeleteView, BrandCreateListAPIView, BrandRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('brand/list/', BrandListView.as_view(), name='brand_list'),
    path('brand/create/', BrandCreateView.as_view(), name='brand_create'),
    path('brand/<int:pk>/detail/', BrandDetailView.as_view(), name='brand_detail'),
    path('brand/<int:pk>/update/', BrandUpdateView.as_view(), name='brand_update'),
    path('brand/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),

    path('api/v1/brands/', BrandCreateListAPIView.as_view(), name='brand_api_list'),
    path('api/v1/brands/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand_api_detail'),
]