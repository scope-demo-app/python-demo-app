import json

from django.http import JsonResponse
from django.views import View
from api.models import Rating
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



class RestaurantsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RestaurantsView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return JsonResponse({'foo': 'bar'})

    def post(self, request):
        new_rating_data = json.loads(request.body)
        new_rating = Rating.objects.create(rating=new_rating_data['rating'], restaurant=new_rating_data['restaurant'])

        return JsonResponse(data={'id': new_rating.id, 'rating':new_rating.rating})