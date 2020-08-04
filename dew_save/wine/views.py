from django.shortcuts import render
from .models import Wine
from .forms import WineForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request, 'wine/home.html')

class Add_wine(LoginRequiredMixin,CreateView):
    model = Wine
    form_class = WineForm
    template_name = 'wine/add_wine.html'
    success_url = reverse_lazy('wine:add')

class All_wine(LoginRequiredMixin,ListView):
    model = Wine
    template_name = 'wine/all_wine.html'
    paginate_by = 5
    queryset = Wine.objects.order_by('-id')

class Detail_wine(LoginRequiredMixin,DetailView):
    model = Wine
    template_name = 'wine/detail_wine.html'

class Delete_wine(LoginRequiredMixin,DeleteView):
    model = Wine
    template_name = 'wine/detail_wine.html'
    success_url = reverse_lazy('wine:add')