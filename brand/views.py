from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from brand.models import Brand
from brand.forms import BrandForm
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework import generics, permissions
from brand.serializers import BrandSerializer


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10
    permission_required = 'brand.view_brand'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset
    

class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')
    permission_required = 'brand.add_brand'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Brand created successfully!')
        context = self.get_context_data(form=form, success=True)
        return self.render_to_response(context)


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    context_object_name = 'brand'
    permission_required = 'brand.view_brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')
    permission_required = 'brand.change_brand'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, 'Brand updated successfully!')
        context = self.get_context_data(form=form, success=True)
        return self.render_to_response(context)
    

class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')
    context_object_name = 'brand'
    permission_required = 'brand.delete_brand'


class BrandCreateListAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes  = [permissions.IsAuthenticated]


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]
