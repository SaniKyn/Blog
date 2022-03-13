from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Наследование
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from taggit.models import Tag

from .models import Post, Comment


class BlogListView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'home.html'


class PostsByAuthorView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'home.html'

    # https://docs.djangoproject.com/en/3.2/topics/db/queries/
    def get_queryset(self):
        author_id = self.kwargs["author_id"]
        return Post.objects.filter(author__id=author_id)


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body', 'header_image', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.is_staff


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.is_superuser


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HomePageView(ListView):
    model = Post
    template_name = 'home'


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    common_tags = Post.tags.most_common()[:4]
    context = {
        'tag': tag,
        'common_tags': common_tags,
    }
    return render(request, 'home.html', context)

