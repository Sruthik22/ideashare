from django.shortcuts import render
from models import Post
from forms import PostForm, UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def main(request):
	loginform = AuthenticationForm()
	create_user_form = UserForm()
	posts=Post.objects.all()
	return render(request,"ideas/index.html",{"posts":posts,"loginform":loginform, "userform": create_user_form})
def yourideas(request):
	form = PostForm()
	posts=Post.objects.filter(author = request.user)
	return render(request, "ideas/yourideas.html", {"form" : form, "posts" : posts})
def newpost(request):
	form = PostForm(request.POST)
	if form.is_valid():
		post = form.save(commit = False)
		post.author = request.user
		post.save()
		return main(request)
def userlogin(request):
	print request.POST
	user = authenticate(username = request.POST['username'], password = request.POST['password'])
	if user:
		login(request, user)
		return HttpResponseRedirect('ideas')
def userlogout(request):
	print request
	logout(request)
	return HttpResponseRedirect('ideas')

def createnewuser(request):
	if request.method == 'POST':
		userform = UserForm(data = request.POST)
	if userform.is_valid():
		user = userform.save()
		user.set_password(user.password)
		user.save()
	return HttpResponseRedirect('ideas')

@login_required
def upvote(request):
	if request.method == 'POST':
		mypost = Post.objects.get(id = request.POST["postid"])
		mypost.votes += 1
		mypost.save()
		return HttpResponse(200)
@login_required
def downvote(request):
	if request.method == 'POST':
		mypost = Post.objects.get(id = request.POST["postid"])
		mypost.votes -= 1
		mypost.save()
		return HttpResponse(200)