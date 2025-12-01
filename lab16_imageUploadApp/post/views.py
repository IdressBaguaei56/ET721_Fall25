from django.views.generic import ListView, CreateView
from .models import Post


class HomePageView(ListView):
    # Show all posts on the home page
    model = Post
    template_name = "home.html"
    context_object_name = "object_list"


class CreatePostView(CreateView):
    # Form to upload a new image + title
    model = Post
    template_name = "post.html"
    fields = ["title", "image"]
    success_url = "/"
