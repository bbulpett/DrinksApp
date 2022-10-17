from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

# Create endpoints
def drink_list(request):

    # get all the drinks
    drinks = Drink.objects.all()

    # serialize them
    serializer = DrinkSerializer(drinks, many=True)

    # return json (set `safe=False` unless returning as an object)
    return JsonResponse({"drinks": serializer.data})
