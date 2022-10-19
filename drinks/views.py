from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create decorator
@api_view(['GET', 'POST'])

# Create endpoints
def drink_list(request):

    # GET request to "Read" all the drinks
    if request.method == 'GET':
        # get all the drinks
        drinks = Drink.objects.all()

        # serialize them
        serializer = DrinkSerializer(drinks, many=True)

        # return json (set `safe=False` unless returning as an object)
        return JsonResponse({"drinks": serializer.data})

    # POST request to "Create" a drink
    if request.method == 'POST':
        # serialize an object of data sent in request
        serializer = DrinkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
