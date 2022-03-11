from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body', 'header_image']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = '__all__'


class HomePageView(ListView):
    model = Post
    template_name = 'home'
