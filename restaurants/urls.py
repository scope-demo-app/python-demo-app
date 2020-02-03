from django.contrib import admin
from django.urls import path
from api.views import RestaurantsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', RestaurantsView.as_view()),
]
