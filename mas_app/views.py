from django.shortcuts import render

# to show the home.html
def home(requests):
    return render(requests,'home.html')

def featuress(requests):
    return render(requests,'featuress.html')

def pricing(requests):
    return render(requests,'pricing.html')
