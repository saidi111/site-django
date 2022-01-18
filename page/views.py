from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return  render(request,'contact.html')
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