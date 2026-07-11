from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == 'POST':
        total_corn = float(request.POST['total_corn'])
        total_soybeans = float(request.POST['total_soybeans'])
        bushels_corn = float(request.POST['bushels_corn'])
        bushels_beans = float(request.POST['bushels_beans'])

        price_corn = 5.35
        price_beans = 11.50
        total_revenue = (total_corn * bushels_corn * price_corn) + (total_soybeans * bushels_beans * price_beans)


        return render(request, 'calculator/home.html', {'total_revenue': total_revenue})
    else:
        return render(request, 'calculator/home.html')

