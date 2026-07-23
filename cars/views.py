from django.db.models import Q
from django.shortcuts import redirect, render
from django.views import View

from cars.forms import CarForm
from cars.models import Car


class CarsView(View):
    def get(self, request):
        search = request.GET.get("search")

        if search:
            cars = Car.objects.filter(
                Q(model__icontains=search) | Q(brand__name__icontains=search)
            ).order_by("model")
        else:
            cars = Car.objects.all().order_by("model")

        return render(request, "cars.html", {"cars": cars})


class NewCarView(View):
    def get(self, request):
        new_car_form = CarForm()
        return render(request, "new-car.html", {"new_car_form": new_car_form})

    def post(self, request):
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect("cars_list")
