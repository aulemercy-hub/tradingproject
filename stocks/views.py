from django.shortcuts import render 

def home(request):
    return render(request, 'stocks/index.html')

def pricing(request):
    return render(request, 'stocks/pricing.html')

def start_analyzing(request):
    return render(request, 'stocks/start_analyzing.html')

def blog_details(request):
    return render(request, 'stocks/blog-details.html')
