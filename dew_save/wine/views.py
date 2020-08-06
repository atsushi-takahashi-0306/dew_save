from django.shortcuts import render
from .models import Wine
from .forms import WineForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect




def home(request):
    if request.user.is_authenticated:
        return redirect('wine:add')
    else:
        return render(request, 'wine/home.html')


class My_wine(LoginRequiredMixin,ListView):
    model = Wine
    template_name = 'wine/my_wine.html'
    paginate_by = 5
    def get_queryset(self):
        return Wine.objects.filter(user=self.request.user)


class Add_wine(LoginRequiredMixin,CreateView):
    model = Wine
    form_class = WineForm
    template_name = 'wine/add_wine.html'
    success_url = reverse_lazy('wine:add')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Add_wine, self).form_valid(form)

class All_wine(LoginRequiredMixin,ListView):
    model = Wine
    template_name = 'wine/all_wine.html'
    paginate_by = 5
    queryset = Wine.objects.order_by('-id')

class Detail_wine(LoginRequiredMixin,DetailView):
    model = Wine
    form_class = WineForm
    template_name = 'wine/detail_wine.html'

class Delete_wine(LoginRequiredMixin,DeleteView):
    model = Wine
    template_name = 'wine/update_wine.html'
    success_url = reverse_lazy('wine:add')

class Update_wine(LoginRequiredMixin,UpdateView):
    model = Wine
    form_class = WineForm
    template_name = 'wine/update_wine.html'
    def get_success_url(self):
        args=self.object.id
        return reverse_lazy('wine:update', args=(self.object.id,))