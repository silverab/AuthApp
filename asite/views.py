from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
	count = User.objects.count()

	context = {'count': count}
	return render(request, 'home.html', context)



def SignUp(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserCreationForm()
	context = {'form': form }
	return render(request, 'registration/signup.html', context)
