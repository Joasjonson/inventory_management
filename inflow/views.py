from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from inflow.models import Inflow
from inflow.forms import InflowForm
from django.contrib import messages
from rest_framework import generics, permissions
from inflow.serializers import InflowSerializer


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflow.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(product__title__icontains=search)
        return queryset
    

class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Inflow
    form_class = InflowForm
    template_name = 'inflow_create.html'
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflow.add_inflow'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Inflow created successfully!')
        context = self.get_context_data(form=form, success=True)
        return self.render_to_response(context)


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'inflow'
    permission_required = 'inflow.view_inflow'


# API Views
class InflowListCreateAPIView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
    permission_classes = [permissions.IsAuthenticated]


class InflowRetrieveAPIAView(generics.RetrieveAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
    permission_classes = [permissions.IsAuthenticated]

    