from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm



class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "account/signup.html" 
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        user = form.save() 
        login(self.request, user)
        self.object = user 
        return HttpResponseRedirect(self.get_success_url())