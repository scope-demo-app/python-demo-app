from django.contrib import admin
from django.urls import path
from api.views import RatingsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ratings/<restaurant>', RatingsView.as_view(), name='ratings'),
]
