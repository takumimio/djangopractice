from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, MyForm, CommentForm
from django.shortcuts import redirect
from django.http import HttpResponse
import json

def ajax_list(request):
    a = range(100)
    return HttpResponse(json.dumps(a), content_type='application/json')
 
def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')

def post_list(request):
	posts = Post.objects.all().order_by('-published_date')[0:5]
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	if request.method == "GET":
		comments = Comment.objects.filter(post_id=pk)
		comments_count = comments.count()
		post = get_object_or_404(Post, pk=pk)
		form = CommentForm()
		return render(request, 'blog/post_detail.html', {'post':post, 'form':form, 'comments':comments, 'comments_count':comments_count})
	else:
		post = get_object_or_404(Post, pk=pk)
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
			return redirect('blog.views.post_detail', pk=post.pk)

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.publish()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})

def post_history(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_history.html', {'posts':posts})

def post_projects(request):
	posts = Post.objects.filter(post_type=2).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.publish()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})

def post_delete(request, pk):
	#post = get_object_or_404(Post, pk=pk)
	post = Post.objects.get(id=pk)
	post.delete()
	return redirect('/blog/')


#測試用view
def test(request):
	form = MyForm()
	return render(request, 'blog/test.html', {'form':form})



