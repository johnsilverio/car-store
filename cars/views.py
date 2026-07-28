from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

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


class CarDetailView(DetailView):
    model = Car
    template_name = "car-detail.html"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "new-car.html"
    success_url = "/cars"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = "car-update.html"

    def get_success_url(self):
        return str(reverse_lazy("car_detail", kwargs={"pk": self.object.pk}))


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarDeleteView(DeleteView):
    model = Car
    template_name = "car-delete.html"
    success_url = "/cars/"
