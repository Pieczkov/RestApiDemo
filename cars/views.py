from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from cars.models import Car, CarType


class CarListView(View):
    def get(self, request):
        cars = Car.objects.all()
        car_types = CarType.objects.all()
        return render(request, "car_list.html", {'cars': cars, "car_types": car_types})


class GetCarByTypeApi(View):

    def get(self, request):
        ids = request.GET.getlist('type_ids')      #pobiera wszytkie 'type_id' ze strony i zamienia na liste
        cars = Car.objects.filter(type__in=ids)   # lookoup in wyszukuje elementy znajdujace sie w ids, i on wie juz ze chodzi o id
        cars = list({"name": car.name, "type": car.type.name} for car in cars)
        print(cars)
        # return HttpResponse(str(cars))               #   dodajemy str by byly z przecinkiem
        # return render(request, 'api_cars.html', {'cars': cars})  # to co ty przekazujemy jest paszka ktora ma dotrzac na strone W naszym przyadku jet to cala strona html w nia nie wolno juz ingerowac
        return JsonResponse(cars, save=True)