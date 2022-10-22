from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create decorator
@api_view(['GET', 'POST'])

# Create endpoints
# (allow format to show raw JSON in browser)
def drink_list(request, format=None):

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


# Create view to show specific model ("show page"), update, or delete
@api_view(['GET', 'PUT', 'DELETE'])

# (allow format to show raw JSON in browser)
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)  # Primary key = ID parameter
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

	# GET request to show specific object
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)

        return Response(serializer.data)
	# PUT request to edit/update specific object
    elif request.method == 'PUT':
        # Accepts JSON request data
        serializer = DrinkSerializer(drink, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        # Respond with Bad Request if invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	# DELETE request to delete specific object
    elif request.method == 'DELETE':
        drink.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
