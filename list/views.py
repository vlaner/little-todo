from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import RegisterForm, ToDoListModelForm
from .models import ToDoListModel


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')


class HomeView(LoginRequiredMixin, ListView):
    model = ToDoListModel
    template_name = 'home.html'
    form_class = ToDoListModelForm

    def get_queryset(self, **kwargs):
        return ToDoListModel.objects.filter(
            user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = ToDoListModel
    fields = ['title']
    template_name = 'makepost.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePostView, self).form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = ToDoListModel
    template_name = 'updatePost.html'
    fields = ['title', 'isDone']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterView, self).get(*args, **kwargs)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = ToDoListModel
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')
    context_object_name = 'task'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
