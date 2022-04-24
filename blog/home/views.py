from turtle import title
from django.shortcuts import get_object_or_404, render
from .models import *
from .decorator import *
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
# Create your views here.


def home(request):

    context = {'blogs': BlogModel.objects.filter(features_fild=False).order_by(
        '-created_at')[:4], 'blog1': BlogModel.objects.filter(features_fild=True).latest()}
    return render(request, 'home.html', context)


def blog_detail(request, slug):
    context = {}
    blog_obj = BlogModel.objects.filter(slug=slug).first()
    post = get_object_or_404(BlogModel, slug=slug)
    comments = post.comments.filter(status=True)
    comments1 = post.comments.filter(status=True).count()
    context = {"blog_obj": blog_obj,
               "comments": comments, "comments1": comments1}

    if request.method == 'POST':
        #data = request.POST.get('name', 'body')
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    return render(request, 'blog_details.html', context)


@unauthenticated_user
def login_logic(request):
    return render(request, 'login.html')


@login_required
@allwed_users(allowed_roles='creators')
def admin_page(request):
    return render(request, 'profile.html')
