from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views.generic.base import View
from catalog.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserPostForm, CommentForm
from .models import User, Post, Comment, Likes
from django.contrib import auth
from django.urls import reverse
from django.shortcuts import get_object_or_404




# Create your views here.
def index(request):

    return render(
        request,
        'index.html')

def about(request):

    return render(
        request,
        'catalog/nav/about.html')

def help(request):

    return render(
        request,
        'catalog/nav/help.html')

def developer(request):

    return render(
        request,
        'catalog/nav/developer.html')

def profile(request):

    return render(
        request,
        'profile.html')

def home(request):

    return render(
        request,
        'profile/home.html')

def photo(request):

    return render(
        request,
        'profile/photogallery.html')

def messager(request):

    return render(
        request,
        'profile/messager.html')





#@login_required
#def profile_view(request):
#    return render(request, 'catalog/profile.html')

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return render(request, 'profile.html')

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            #return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            #return render(request, 'profile.html')
            return HttpResponseRedirect(reverse('catalog:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'profile/editprof.html', context)





#def full_slug(reguest, pk):
#    comment_form = CommentForm
#    form = comment_form
#    te = get_object_or_404(Post, id=pk)
#    comments = Comment.objects.filter(post=te)
#    return render(reguest, 'full.html', {'te': te, 'form': form, 'comments': comments, 'username': auth.get_user(reguest).username})

@login_required
def new_post(request):
    if request.method == 'POST':
        form = UserPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(reverse('catalog:profile'))
            #return render(request, 'profile.html')
    else:
        form = UserPostForm()
    context = {'form': form}
    return render(request, 'profile/post.html', context)

#def success(request):
#    return render(request, 'profile.html')
    #return reverse('catalog:profile')

#@login_required
#@require_http_methods(["POST"])
#def post_getail(request, pk):
    #post_comm = get_object_or_404(Post, id=pk)
#    if request.method == 'POST':
#        form = CommentForm(data=request.POST, files=request.FILES)
#        post = Post.objects.get(id=pk)
##        if form.is_valid():
 #           comment = form.save(commit=False)
 #           comment.post = post
 #           comment.name = request.user
 #           comment.save()
 #           return HttpResponseRedirect(reverse('catalog:profile'))
            #return render(request, 'profile.html')
 #   else:
 #       form = CommentForm()
 #   posts = Post.objects.all()
 #   context = {'posts': posts, 'form': form}
 #   return render(request, 'profile/comment.html', context)

class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'profile/comment.html', {'post': post})

class AddComments(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.author = request.user
            comment.pos_id = int(pk)
            comment.save()
        return redirect('catalog:profile')
        #return redirect(request.META['HTTP_REFERER'])
            #return render(request, 'profile.html')
        #else:
        #    form = CommentForm()
        #    post_id = Post.object.all()
        #context = {'post_id': post_id, 'form': form}
        #return render(request, 'profile/comment.html', context)

class PostView(View):
    def view_users(self, request):
        users_list = User.objects.all()
        context = {'users_list': users_list}
        return render(request, 'profile.html', context)
    def get(self, request):
        posts = Post.objects.all().filter(user=request.user).order_by('-date')
        #count = Post.objects.all().filter(user=request.user).count()
        #comments = Comment.objects.all().filter(pos_id=request.POST.get('post_id')).order_by('-created')
        #postss = Post.objects.all()
        comments = Comment.objects.all().order_by('-created')
        context = {'post_list': posts, 'comment_list': comments}
        return render(request, 'profile.html', context)


class PostViewHome(View):

    def get(self, request):
        posts = Post.objects.all().order_by('-date')
        comments = Comment.objects.all().order_by('-created')
        context = {'post_lists': posts, 'comment_list': comments}
        #context = {'post_lists': posts}
        return render(request, 'profile/home.html', context)


#def get_client_ip(request):
#    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#    if x_forwarded_for:
#        ip = x_forwarded_for.split(',')[0]
#    else:
#        ip = request.META.get('REMOTE_ADDR')
#    return ip


#class AddLike(View):
#    def get(self, request, pk):
#        id_client = request.user.id
#        try:
#            Likes.objects.get(id=id_client, pos_id=pk)
#            return HttpResponseRedirect(reverse('catalog:profile'))
#        except:
#            new_like = Likes()
#            #new_like.id = id_client
#            new_like.pos_id = int(pk)
#            new_like.save()
#            return HttpResponseRedirect(reverse('catalog:profile'))





@login_required
def hit_like_button(request, pk):
    post = get_object_or_404(Post, pk=pk)
    liked_post, created = Likes.objects.get_or_create(
        pos=post,
        user_like=request.user
    )
    if not created:
        liked_post.delete()

    else:
        liked_post.save()

    return HttpResponseRedirect(reverse('catalog:profile'))

@login_required
def home_like_button(request, pk):
    post = get_object_or_404(Post, pk=pk)
    liked_post, created = Likes.objects.get_or_create(
        pos=post,
        user_like=request.user
    )
    if not created:
        liked_post.delete()

    else:
        liked_post.save()

    return HttpResponseRedirect(reverse('catalog:home'))




class PostDelete(View):
    def get(self, request, pk):
            post = Post.objects.get(id=pk)
            post.delete()
            return HttpResponseRedirect(reverse('catalog:profile'))






