from django.shortcuts import render
from models import Post
# Create your views here.
def main(request):
	posts=Post.objects.all()
	return render(request,"ideas/index.html",{"posts":posts})
