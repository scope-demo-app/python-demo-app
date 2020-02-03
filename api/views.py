import json

from django.http import JsonResponse
from django.views import View
from django.core import serializers
from api.models import Restaurant
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



class RestaurantsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RestaurantsView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        data = serializers.serialize("json", Restaurant.objects.all())
        return JsonResponse(data=data, safe=False)

    def post(self, request):
        new_restaurant_data = json.loads(request.body)
        new_restaurant = Restaurant.objects.create(name=new_restaurant_data['name'], description=new_restaurant_data['description'])

        return JsonResponse(data={'id':new_restaurant.id, 'name': new_restaurant.name, 'description': new_restaurant.description}, safe=False)