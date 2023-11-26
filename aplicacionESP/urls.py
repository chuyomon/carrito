from django.urls import path, include
from rest_framework import routers
from PruebaESP.viewsets import MembersViewSet
from . import views

route = routers.SimpleRouter()
route.register('aplicacionESP', MembersViewSet)



urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    # Incluir las URLs generadas por el enrutador utilizando include y las URLs directas
    path('', include(route.urls)),
]
