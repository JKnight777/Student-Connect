from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        # 'title': post.title,
        # 'author': post.author,
        # 'text': post.text #old inefficient way, pass whole object instead.
        'post': post,
    }
    return render(request, "posts/detail.html", context)


def post_creation_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, "posts/create.html", context)

def post_list_view(request):
    set = Post.objects.all()
    context = {
        'object_list': set #called object_list by convention and for reusability
    }

    return render(request, "posts/list.html", context)