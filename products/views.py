from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from products.models import ProductModel, CategoryModel


def home_page(request):
    return render(request, "index.html",)
class Shop_page(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.all().order_by('price')
    context_object_name = "products"
    paginate_by = 1

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Категория'] = CategoryModel.objects.all()
        return context


class  Shop_page_Detail(DetailView):
    template_name = 'shop-details.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'
class RegisterView(TemplateView):
    template_name = 'signup.html'


class LoginView(TemplateView):
    template_name = 'login.html'

