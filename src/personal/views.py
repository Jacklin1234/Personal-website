from django.shortcuts import render

from .models import person

from .forms import personForm
# Create your views here.
def base(request):
	print(request.user)
	return render(request, 'personal/base.html',{})


def about(request):
	obj = person.objects.get(id=3)
	about_context={
		"firstname":obj.firstname,
		"lastname":obj.lastname,
		"age":obj.age,
		"gender":obj.gender
	}
	return render(request,'personal/about.html',about_context)

def contact(request):
	return render(request,'personal/contact.html',{})

def signup(request):
	form = personForm(request.POST or None)
	if form.is_valid():
		form.save()
	conext = {
		'form' : form
	}

	return render(request,'personal/signup.html',conext)

def login(request):
	return render(request,'personal/login.html',{})