from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Blog,Comment
from .forms import BlogForm,CommentForm

# Create your views here.

# ----------------- LIST VIEW --------------------

class Home(ListView):
    model = Blog
    template_name = "index/home.html"
    ordering = ['-id']
    paginate_by = 5

# ----------------- DETAIL VIEW --------------------


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'index/readmore.html'

# ----------------- ADD VIEW --------------------


class AddBlog(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = "index/addblog.html"
    # fields = "__all__"
    
# ----------------- EDIT VIEW --------------------

class EditBlog(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "index/update.html"
    # fields = "__all__"

# ----------------- DELETE VIEW --------------------

class DeleteBlog(DeleteView):
    model = Blog
    template_name = "index/delete.html"
    success_url = reverse_lazy("home")

# ----------------- COMMENT VIEW --------------------

# class AddComment(CreateView):
#     model = Comment
#     form_class = EditComment
#     template_name = "index/addcomment.html"
#     success_url = reverse_lazy("home")


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'index/addcomment.html'  
    success_url = reverse_lazy('blog:addcomment') 
    
    def form_valid(self, form):
        form.instance.blogpost = get_object_or_404(Blog, id=self.kwargs['id'])
        return super().form_valid(form)
    
    
    