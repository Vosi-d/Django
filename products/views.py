from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from products.models import ProductModel


def home_page(request):
    return render(request, "index.html",)

# def shop_page(request):
#     # products = ProductModel.objects.all().filter(title="iphone15")
#     products = ProductModel.objects.all().order_by('price')
#     return render(request, "shop.html", {"products": products})
class Shop_page(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.all().order_by('price')
    context_object_name = "products"

    def get_queryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs
class  Shop_page_Detail(DetailView):
    template_name = 'shop-details.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'

class RegisterView(TemplateView):
    template_name = 'signup.html'


class LoginView(TemplateView):
    template_name = 'login.html'

