from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=30)
	date_time = models.DateField(auto_now_add=True)
	main_img = models.FileField()
	main_text = models.TextField()
	cate = models.CharField(max_length=30)
	url_pat = models.CharField(max_length=30, default = 'null' )
	
class Detail(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	img1 = models.FileField()
