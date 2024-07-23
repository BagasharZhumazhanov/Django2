from django.shortcuts import render

def index(request):    
    products = [
        {"id": 1, "name": "Adidas", "quantity": 5},
        {"id": 2, "name": "Nike", "quantity": 3},
        {"id": 3, "name": "Sprite", "quantity": 7},
        {"id": 4, "name": "Coca-cola", "quantity": 4}
    ]
    return render(request, 'index.html', {'products': products})



    


