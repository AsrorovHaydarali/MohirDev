from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Comment

from django.urls import reverse_lazy

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class CommentListView(ListView):
    model = Comment
    template_name = "comment_list.html"
    context_object_name = "comment_list"


class CommentDetailView(DetailView):
    model = Comment
    template_name = "comment_detail.html"


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "comment_create.html"
    fields = ("comment",)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = "comment_update.html"
    fields = ("comment",)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comment_delete.html"
    success_url = reverse_lazy("comment_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


def custom_403(request, exception):
    return render(request, "403.html", status=403)
