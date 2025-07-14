from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import TemplateView, DetailView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='user:login')
def dashboard(request):
    products = Product.objects.filter(sold_out=False)[:8]
    context = {
        'products': products,
        'items': products.count(),
    }
    return render(request, 'store/dashboard.html', context)


def get_result(search_info, search_type):
    if search_type == "Product":
        return Product.objects.filter(
            name__icontains=search_info
        )
    elif search_type == "Category":
        return ProductCategory.objects.get(
            name__icontains=search_info
        )


@login_required(login_url='user:login')
def search_func(request):
    search_info = request.POST['search_info']
    search_type = request.POST['search_type']
    result = get_result(search_info, search_type)
    context = {
        'result': result,
        'search_type': search_type,
        'info': search_info,
    }
    return render(request, 'store/search_result.html', context)


@login_required(login_url='user:login')
def add_category(request):
    form = AddCategoryForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddCategoryForm()
    context = {
        'form': form
    }
    return render(request, 'store/add_category.html', context)


@login_required(login_url='user:login')
def add_colour(request):
    form = AddColourForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddColourForm()
    context = {
        'form': form
    }
    return render(request, 'store/add_colour.html', context)


class AddProduct(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        form = AddProductForm()
        context = {
            'form': form,
        }
        return render(self.request, 'store/add_product.html', context)

    def post(self, request, *args, **kwargs):
        form = AddProductForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            color = form.cleaned_data.get('color')
            details = form.cleaned_data.get('detail')
            imei = form.cleaned_data.get('imei')
            spec = form.cleaned_data.get('spec')
            type = form.cleaned_data.get('type')
            print(name, color, details, imei, spec, type)

            new_product, created = Product.objects.get_or_create(
                name=name,
                color=color,
                details=details,
                imei=imei,
                spec=spec,
                type=type,
                checked_in=True,
                checked_in_date=timezone.now()
            )
            return redirect('/')
        else:
            return redirect('/')
