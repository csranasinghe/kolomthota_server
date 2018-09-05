from django.shortcuts import render


def index(request):
    return render(request, 'shipping_line/index.html', {})