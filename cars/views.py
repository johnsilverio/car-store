from django.db.models import Q
from django.views.generic import CreateView, ListView

from cars.forms import CarForm
from cars.models import Car


class CarsListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")

        if search:
            cars = cars.filter(
                Q(model__icontains=search) | Q(brand__name__icontains=search)
            ).order_by("model")
        return cars


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "new-car.html"
    success_url = "/cars"
