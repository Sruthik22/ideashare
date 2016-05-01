from django.forms import ModelForm, PasswordInput, CharField
from .models import Post
from django.contrib.auth.models import User

# Create the form class.
class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title','content']

class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')