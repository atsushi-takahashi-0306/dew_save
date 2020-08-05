from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import redirect


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "account/signup.html" 
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        user = form.save() 
        login(self.request, user)
        self.object = user 
        return HttpResponseRedirect(self.get_success_url())

class Delete_user(UserPassesTestMixin,DeleteView):
    model = User
    template_name = 'account/account.html'
    success_url = reverse_lazy('wine:home')

class Update_user(UpdateView):
    model = User
    form_class = SignUpForm
    template_name = 'account/account.html'
    def get_success_url(self):
        args=self.object.id
        return reverse_lazy('account:update', args=(self.object.id,))