from django.http import JsonResponse
from django.views import View

class RestaurantsView(View):
    def get(self, request):
        return JsonResponse({'foo':'bar'})