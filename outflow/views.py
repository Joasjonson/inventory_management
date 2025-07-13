from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from app import metrics
from outflow.models import Outflow
from outflow.forms import OutflowForm
from django.contrib import messages
from rest_framework import generics, permissions
from outflow.serializers import OutflowSerializer


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflow.view_outflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(product__title__icontains=search)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context

class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    form_class = OutflowForm
    template_name = 'outflow_create.html'
    success_url = reverse_lazy('outflow_list')
    permission_required = 'outflow.add_outflow'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Outflow created successfully.')
        context = self.get_context_data(form=form, success=True)
        return self.render_to_response(context)
    

class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'
    context_object_name = 'outflow'
    permission_required = 'outflow.view_outflow'


class OutflowListCreateAPIView(generics.ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer 
    permission_classes = [permissions.IsAuthenticated]


class OutflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer
    permission_classes = [permissions.IsAuthenticated]