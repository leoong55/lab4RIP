from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def function_view(request):
    return HttpResponse('response form function view')

class ExampleClassBase(View):
    def get(self, request):
        return HttpResponse('response from class based view')

class ExampleView(View):
    def get(self, request):
        return render(request, 'base.html')

class OrdersView(View):
    def get(self, request):
        data = {
            'orders': [
                {'title': 'First order', 'id': 1},
                {'title': 'Second order', 'id': 2},
                {'title': 'Third order', 'id': 3},
            ]
        }
        return render(request, 'orders.html', data)

class EmptyOrdersView(View):
    def get(self, request):
        data = {
            'orders': []
        }
        return render(request, 'orders.html', data)

class OrderView(View):
    def get(self, request, id):
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', data)