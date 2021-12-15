from django.shortcuts import render, get_object_or_404
from .models import Post, Detail

def  index (request):
	post_pc =  Post.objects.order_by('-date_time')
	
	return render (request, 'home.html', {'post_pc':post_pc})

def about (request):
	return render (request, 'about.html')

def detail(request, post_urls):
	posts = Post.objects.all()
	post_id = 0
	for pot in posts:
		if post_urls == pot.url_pat:
			post_id = pot.pk

	post = get_object_or_404(Post, pk = post_id)
	return render (request, 'detail.html', {'post': post})