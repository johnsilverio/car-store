from django import forms

from cars.models import Car


class StyledClearableFileInput(forms.ClearableFileInput):
    template_name = "widgets/clearable_file_input.html"


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "photo": StyledClearableFileInput(),
        }

    def clean_value(self):
        value = self.cleaned_data.get("value")
        if value is not None and value < 20000:
            self.add_error("value", "Valor mínimo do carro deve ser de R$20.000,00")
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get("factory_year")
        if factory_year is not None and factory_year < 1975:
            self.add_error(
                "factory_year",
                "Não é permitido cadastrar carros fabricados antes de 1975.",
            )
        return factory_year
