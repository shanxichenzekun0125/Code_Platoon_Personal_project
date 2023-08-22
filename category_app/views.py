from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



# def all_transaction(request):
#     transactions = TransactionSerializer(Transaction.objects.order_by('time'), many=True)
#     return JsonResponse({"All Transactions": transactions.data })

class All_category(APIView):
    def get(self, request):
        categories = CategorySerializer(Category.objects.all(), many=True)
        return Response({"All Categories": categories.data })