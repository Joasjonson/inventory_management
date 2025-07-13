from django.urls import path
from inflow.views import InflowListView, InflowCreateView, InflowDetailView, InflowListCreateAPIView, InflowRetrieveAPIAView

urlpatterns = [
    path('inflow/list/', InflowListView.as_view(), name='inflow_list'),
    path('inflow/create/', InflowCreateView.as_view(), name='inflow_create'),
    path('inflow/<int:pk>/detail/', InflowDetailView.as_view(), name='inflow_detail'),

    # API endpoints
    path('api/v1/inflow/', InflowListCreateAPIView.as_view(), name='inflow_api_list_create'),
    path('api/v1/inflow/<int:pk>/', InflowRetrieveAPIAView.as_view(), name='inflow_api_detail'),
]