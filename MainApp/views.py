from django.shortcuts import render
from .models import Item

def index(request):    
    products = [
        {"id": 1, "name": "Adidas", "quantity": 5},
        {"id": 2, "name": "Nike", "quantity": 3},
        {"id": 3, "name": "Sprite", "quantity": 7},
        {"id": 4, "name": "Coca-cola", "quantity": 4}
    ]
    return render(request, 'index.html', {'products': products}) 


def products(request):
    items = Item.objects.all()
    return render_to_response("products.html", {'place_of_work':[Item.organization for item in items]})






    


