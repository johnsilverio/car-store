from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts.views import login_view, logout_view, register_view
from app import settings
from cars.views import CarsView, NewCarView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("cars/", CarsView.as_view(), name="cars_list"),
    path("new-car/", NewCarView.as_view(), name="new_car"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
