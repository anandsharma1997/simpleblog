from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post ,Category
from .form import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.

#simply rendering home page here
# def home(request):
#     return render(request, 'home.html')

#here is home page showing all the posts
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']
    ordering = ['post_date']

#here is the article details page where specific post will be shown
class ArticleDetailsView(DetailView):
    model=Post
    template_name = 'article_details.html'


#here is add post page 
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  #  fields = '__all__'

#here is adding categary list
class CreateCategaryView(CreateView):
    model = Category
    template_name = 'add_categary.html'
    fields = '__all__'


#here is update post page
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
   # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


#show categories here

def CategaryView(request, cats):
    categary_posts = Post.objects.filter(categary=cats)
    return render(request, "categaries.html", {'cats':cats, 'categary_post': categary_posts})



def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return 
