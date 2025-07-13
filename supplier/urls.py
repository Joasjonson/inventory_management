from django.urls import path
from supplier.views import SupplierListView, SupplierCreateView, SupplierDetailView, SupplierUpdateView, SupplierDeleteView, SupplierListCreateAPIView, SupplierRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('supplier/list/', SupplierListView.as_view(), name='supplier_list'),
    path('supplier/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/detail/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    path('api/v1/supplier/', SupplierListCreateAPIView.as_view(), name='supplier_api_list_create'),
    path('api/v1/supplier/<int:pk>/', SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier_api_detail'),
]