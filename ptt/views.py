from django.shortcuts import render
from .models import Softjob

def post_list(request):
	posts = Softjob.objects.all()
	return render(request, 'ptt/post_list.html', {'posts':posts})

def post_hire(request):
	posts = Softjob.objects.filter(title__contains='[徵才]')
	return render(request, 'ptt/post_list.html', {'posts':posts})

