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


def dashboard(request):
    return render(request, 'store/dashboard.html')
