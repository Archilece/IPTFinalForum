from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from .forms import CreateTopicForm, CreateCommentForm
from .models import Forum, Topic


########################### FORUM
def forums_detail(request, forum_id):
    forum = Forum.objects.get(id=forum_id)
    topics = forum.topic_set.all().order_by('-tdate')
    return render(request, 'forums/forums_detail.html', {'forum': forum, 'topics': topics})

def forums_list(request):
    forums = Forum.objects.all().order_by('-date')
    return render(request, 'forums/forums_list.html', {'forums': forums})

######################## TOPICS
def topic_detail(request, forum_id, topic_id):
    forum = Forum.objects.get(id=forum_id)
    topic = Topic.objects.get(id=topic_id, forum=forum)
    return render(request, 'topics/topic_detail.html', {'forum': forum, 'topic': topic})

@login_required(login_url='forums:login')
def create_topic(request, forum_id):
    forum = Forum.objects.get(id=forum_id)
    if request.method == 'POST':
        form = CreateTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.forum = forum
            topic.tauthor = request.user
            topic.save()
            return redirect('forums:detail', forum_id=forum.id)
    else:
        form = CreateTopicForm()
    return render(request, 'topics/create_topic.html', {'form': form})
################ACOUNTS###################################################
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('forums:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('forums:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('forums:list')
    
@login_required(login_url='forums:login')
def add_comment(request, forum_id, topic_id):
    forum = Forum.objects.get(id=forum_id)  
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.cauthor = request.user 
            try:
                comment.save()
                return redirect('forums:detail', forum_id=forum_id)
            except IntegrityError:
                pass
    else:
        form = CreateCommentForm()
    return render(request, 'topics/add_comment.html', {'form': form, 'topic_id': topic_id, 'forum': forum}) 
