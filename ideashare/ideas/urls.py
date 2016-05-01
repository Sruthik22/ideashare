from views import main,yourideas,newpost,userlogin, userlogout,createnewuser, upvote, downvote
from django.conf.urls import url, include

urlpatterns = [
    url(r'upvote', upvote),
    url(r'downvote', downvote),
	url(r'newuser', createnewuser),
	url(r'newpost',newpost),
	url(r'yourideas', yourideas),
	url(r'login', userlogin),
	url(r'logout', userlogout),
	url(r'^', main),

]