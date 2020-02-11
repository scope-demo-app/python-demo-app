import json

from django.http import JsonResponse
from django.views import View
from api.models import Rating
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Avg


class RatingsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RatingsView, self).dispatch(request, *args, **kwargs)

    def get(self, request, restaurant, *args, **kwargs):
        rating = Rating.objects.filter(restaurant=restaurant).aggregate(Avg('rating'))
        return JsonResponse(
            data={'rating': rating['rating__avg'], 'restaurant': restaurant}
        )

    def post(self, request, restaurant, *args, **kwargs):
        new_rating_data = int(request.body)
        new_rating = Rating.objects.create(
            rating=new_rating_data, restaurant=restaurant
        )
        return JsonResponse(data={'id': new_rating.id, 'rating': new_rating.rating})

