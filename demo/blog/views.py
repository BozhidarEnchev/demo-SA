from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from demo.blog.forms import PostCreateForm
from demo.blog.models import Post, Comment


class PostView(ListView):
    model = Post
    template_name = 'blog/post-dashboard.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post-form.html'
    # success_url = reverse_lazy('post-dashboard')
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post-form.html'
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.object.pk})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-details.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post-delete.html'
    success_url = reverse_lazy('post-dashboard')


def post_comment(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        content = request.POST.get("content")

        post = get_object_or_404(Post, pk=post_id)

        Comment.objects.create(
            post_id=post,
            content=content,
        )

        return redirect('post-details', post.pk)

    return redirect('post-dashboard')


def delete_comment(request, pk):
    if request.method == "POST":
        comment = get_object_or_404(Comment, pk=pk)
        post = comment.post_id
        comment.delete()
        return redirect('post-details', post.id)
    return redirect('post-dashboard')
