from django.shortcuts import render, get_object_or_404
from post.models import Post, Detail

def pc_full(request):
	post_pc =  Post.objects.filter(cate = 'P.C').order_by('-date_time')
	return render (request, 'pc_full.html', {'post_pc': post_pc})

def con_full(request):
	post_con =  Post.objects.filter(cate = 'Console').order_by('-date_time')
	return render (request, 'con_full.html', {'post_con': post_con})
