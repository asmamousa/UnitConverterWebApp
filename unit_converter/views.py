from django.shortcuts import render
from .forms import LengthConverterForm, WeightConverterForm, TemperatureConverterForm

conversion_rates_to_m = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34,
}

conversion_rates_to_g = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "oz": 28.3495,
    "lb": 453.592,
}

def length_converter(request):
    result = None
    if request.method == 'POST':
        form = LengthConverterForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            # convert to meters first
            value_in_meters = value * conversion_rates_to_m[from_unit]

            # convert meters to target unit
            result = value_in_meters / conversion_rates_to_m[to_unit]

        else:
            print(form.errors)

    else:
        form = LengthConverterForm()

    return render(request, 'unit_converter/length.html', context={"form": form, "result": result})


def weight_converter(request):
    result = None
    if request.method == 'POST':
        form = WeightConverterForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            # convert to grams first
            value_in_grams = value * conversion_rates_to_g[from_unit]

            # convert grams to target unit
            result = value_in_grams / conversion_rates_to_g[to_unit]

    else:
        form = WeightConverterForm()

    return render(request, 'unit_converter/weight.html', context={'form': form, 'result': result})



def temperature_converter(request):
    result = None
    if request.method == 'POST':
        form = TemperatureConverterForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']

            # Step 1: convert from source unit to Celsius
            if from_unit == "c":
                value_in_celsius = value
            elif from_unit == "f":
                value_in_celsius = (value - 32) * 5 / 9
            elif from_unit == "k":
                value_in_celsius = value - 273.15

            # Step 2: convert Celsius to target unit
            if to_unit == "c":
                result = value_in_celsius
            elif to_unit == "f":
                result = value_in_celsius * 9 / 5 + 32
            elif to_unit == "k":
                result = value_in_celsius + 273.15

    else:
        form = TemperatureConverterForm()

    return render(request, 'unit_converter/temperature.html', context={'form': form, 'result': result})

