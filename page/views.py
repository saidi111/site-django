from django.shortcuts import render,redirect
from .formulaire import contactForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):

    if request.method == 'POST':

        form=contactForm(request.POST, request.FILES).save()
        return redirect('/home')
    else:
        form=contactForm()
    return  render(request,'contact.html',{'form': form})
def about(request):
    return  render(request,'about.html')
def service(request):
    return  render(request,'service.html')
def projet(request):
    return  render(request,'project.html')
def feature(request):
    return  render(request,'feature.html')
def quote(request):
    return  render(request,'quote.html')
def team(request):
    return  render(request,'team.html')
def testimonial(request):
    return  render(request,'testimonial.html')
def quatre(request):
    return  render(request,'404.html')