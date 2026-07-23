from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import redirect, render

from cars.forms import CarForm
from cars.models import Car


def cars_view(request: HttpRequest):
    search = request.GET.get("search")

    if search:
        cars = Car.objects.filter(
            Q(model__icontains=search) | Q(brand__name__icontains=search)
        ).order_by("model")
    else:
        cars = Car.objects.all().order_by("model")

    return render(request, "cars.html", {"cars": cars})


def new_car_view(request: HttpRequest):
    if request.method == "POST":
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect("cars_list")
    else:
        new_car_form = CarForm()

    return render(request, "new-car.html", {"new_car_form": new_car_form})
