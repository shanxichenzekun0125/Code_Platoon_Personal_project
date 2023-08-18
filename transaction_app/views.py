from django.shortcuts import render
from .models import Transaction
from .serializers import TransactionSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



# def all_transaction(request):
#     transactions = TransactionSerializer(Transaction.objects.order_by('time'), many=True)
#     return JsonResponse({"All Transactions": transactions.data })

class All_transaction(APIView):
    def get(self, request):
        transactions = TransactionSerializer(Transaction.objects.order_by('-time'), many=True)
        return Response({"All Transactions": transactions.data })