from django.shortcuts import render

def home(request):
    return render(request, 'stocks/index.html')

def open_tradingaccount(request):
    return render(request, 'stocks/open_tradingaccount.html')

def pricing(request):
    return render(request, 'stocks/pricing.html')
