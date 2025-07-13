from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from supplier.models import Supplier
from supplier.forms import SupplierForm
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework import generics, permissions
from supplier.serializers import SupplierSerializer


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10
    permission_required = 'supplier.view_supplier'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset
    

class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Supplier
    template_name = 'supplier_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')
    permission_required = 'supplier.add_supplier'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Supplier created successfully!')
        context = self.get_context_data(form=form, success=True)
        return self.render_to_response(context)


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    context_object_name = 'supplier'
    permission_required = 'supplier.view_supplier'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Supplier
    template_name = 'supplier_update.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')
    permission_required = 'supplier.change_supplier'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Supplier updated successfully!')
        context = self.get_context_data(form=form, success=True)
        return self.render_to_response(context)  


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
    context_object_name = 'supplier'
    permission_required = 'supplier.delete_supplier'


class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]
