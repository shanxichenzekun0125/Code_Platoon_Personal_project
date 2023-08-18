from django.shortcuts import render
from .models import Transaction
from .serializers import TransactionSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

# Create your views here.



# def all_transaction(request):
#     transactions = TransactionSerializer(Transaction.objects.order_by('time'), many=True)
#     return JsonResponse({"All Transactions": transactions.data })

class All_transaction(APIView):
    def post(self, request):

        
        new_transaction = TransactionSerializer(data= request.data)
        
        if new_transaction.is_valid():
            new_transaction.save()
            return Response(new_transaction.data, status=HTTP_201_CREATED)
        else:
            return Response(new_transaction.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request):
        transactions = TransactionSerializer(Transaction.objects.order_by('-time'), many=True)
        return Response({"All Transactions": transactions.data })
    

class Select_transaction(APIView):
    def get(self, request, id):
        try:
            transaction = Transaction.objects.get(id=id)
            serializer = TransactionSerializer(transaction)  # Assuming you have a TransactionSerializer defined
            return Response(serializer.data)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=HTTP_404_NOT_FOUND)


    def put(self, request, id):
        transaction = Transaction.objects.get(id=id)
        transaction.money_amount=request.data["money_amount"]
        transaction.location = request.data["location"]
        transaction.note = request.data["note"]

        transaction.full_clean()
        transaction.save()
        return Response(status=HTTP_204_NO_CONTENT)
