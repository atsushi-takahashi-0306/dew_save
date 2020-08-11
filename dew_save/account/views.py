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

from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views import generic


class PasswordReset(PasswordResetView):
    """パスワード変更用URLの送付ページ"""
    subject_template_name = 'account/subject.txt'
    email_template_name = 'account/message.txt'
    template_name = 'account/password_reset_form.html'
    success_url = reverse_lazy('account:password_reset_done')

class PasswordResetDone(PasswordResetDoneView):
    """パスワード変更用URLを送りましたページ"""
    template_name = 'account/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    """新パスワード入力ページ"""
    success_url = reverse_lazy('account:password_reset_complete')
    template_name = 'account/password_reset_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    """新パスワード設定しましたページ"""
    template_name = 'account/password_reset_complete.html'


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "account/signup.html" 
    success_url = reverse_lazy('account:login')

    def form_valid(self, form):
        user = form.save() 
        login(self.request, user)
        self.object = user 
        return HttpResponseRedirect(self.get_success_url())
    

class Delete_user(OnlyYouMixin,DeleteView):
    model = User
    template_name = 'account/account.html'
    success_url = reverse_lazy('wine:home')

class Update_user(OnlyYouMixin,UpdateView):
    model = User
    form_class = SignUpForm
    template_name = 'account/account.html'
    def get_success_url(self):
        args=self.object.id
        return reverse_lazy('account:login')