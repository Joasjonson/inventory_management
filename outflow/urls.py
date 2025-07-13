from django.urls import path
from outflow.views import OutflowListView, OutflowCreateView, OutflowDetailView, OutflowListCreateAPIView, OutflowRetrieveAPIView

urlpatterns = [
    path('outflow/list/', OutflowListView.as_view(), name='outflow_list'),
    path('outflow/create/', OutflowCreateView.as_view(), name='outflow_create'),
    path('outflow/<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),

    path('api/v1/outflow/', OutflowListCreateAPIView.as_view(), name='outflow_api_list_create'),
    path('api/v1/outflow/<int:pk>/', OutflowRetrieveAPIView.as_view(), name='outflow_api_detail'),
    
]