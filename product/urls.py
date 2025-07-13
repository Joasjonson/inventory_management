from django.urls import path
from product.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('api/v1/product/', ProductListCreateAPIView.as_view(), name='product_api_list_create'),
    path('api/v1/product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_api_detail'),
]