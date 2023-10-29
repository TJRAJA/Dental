from django.shortcuts import render
from dapp.models import denal,c_denal,email
from dapp.forms import denalForm,contactForm,emailForm


def home(request):
	form = denalForm()
	if request.method=='POST':
		form = denalForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'Html/home.html',{'form':form})


def about(request):
	return render(request,'Html/about.html')


def service(request):
	return render(request,'Html/service.html')


def price(request):
	return render(request,'Html/price.html')


def team(request):
	return render(request,'Html/team.html')


def testimonial(request):
	return render(request,'Html/testimonial.html')



def appointment(request):
	form = denalForm()
	if request.method=='POST':
		form = denalForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'Html/appointment.html',{'form':form})


def contact(request):
	form = contactForm()
	if request.method=='POST':
		form = contactForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'Html/contact.html',{'form':form})


def email(request):
	form = emailForm()
	if request.method=='POST':
		form = emailForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'Html/index.html',{'form':form})






def viewpage(request):
	denalinfo = denal.objects.all()
	return render(request,'Html/viewpage.html',{'s':denalinfo})
 

def viewpagecontact(request):
	denalcontact = c_denal.objects.all()
	return render(request,'Html/viewpagecontact.html',{'s':denalcontact})


