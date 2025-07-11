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
