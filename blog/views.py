from django.shortcuts import render
from django.views import generic
from .models import Post, Email, Extras
from django.contrib.auth.forms import UserCreationForm
from blog.forms import EmailForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def postList(request):
    queryset = Post.objects.order_by('-created_on')
    mr_post = Post.objects.latest('created_on')
   
    context = {'queryset': queryset, 'mr_post':mr_post}

    return render(request,'blog/home.html',context)

def postDetail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)

def email(request):
    form_class = EmailForm
    # Add a new email:
    form = form_class(request.POST or None)
    if request.method != 'POST':
        form = EmailForm
    else:
        # POST data submitted, process data
        if form.is_valid():
            email = form.save(commit=False)
            email.save()
            return HttpResponseRedirect(reverse('home'))

    context = {'form': form}
    return render(request, 'blog/email.html', context)

def extras(request):
    queryset = Extras.objects.order_by('-created_on')
    context = {'queryset': queryset}

    return render(request, 'blog/extras.html', context)

def extrasDetail(request, slug):
    extras = Extras.objects.get(slug=slug)
    context = {'extras': extras}

    return render(request, 'blog/extras_detail.html', context)

def about(request):
    return render(request, 'blog/about.html')

    