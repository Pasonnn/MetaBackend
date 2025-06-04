from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework.views import APIView

# Create your views here.
class BookList(APIView):
    def get(self, request):
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    
    def post(self, request):
        title = request.data.get('title')
        author = request.data.get('author')
        price = request.data.get('price')
        
        book = Book(title=title, author=author, price=price)
        
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'}, status=400)
        
        return JsonResponse(model_to_dict(book), status=201)