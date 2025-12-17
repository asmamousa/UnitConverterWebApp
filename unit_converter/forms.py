from django import forms

class LengthConverterForm(forms.Form):
    LENGTH_UNITS = [
        ("cm", "Centimeter"),
        ("mm", "Millimeter"),
        ("m", "Meter"),
        ("km", "Kilometer"),
        ("inch", "Inch"),
        ("foot", "Foot"),
        ("yard", "Yard"),
        ("mile", "Mile"),
    ]

    value = forms.FloatField(label='Enter the length to convert')
    from_unit = forms.ChoiceField(choices=LENGTH_UNITS, label="Unit to convert from")
    to_unit = forms.ChoiceField(choices=LENGTH_UNITS, label="Unit to convert to")


class WeightConverterForm(forms.Form):
    WEIGHT_UNITS = [
        ("mg", "Milligram"),
        ("g", "Gram"),
        ("kg", "Kilogram"),
        ("oz", "Ounce"),
        ("lb", "Pound"),
    ]

    value = forms.FloatField(label='Enter the weight to convert')
    from_unit = forms.ChoiceField(choices=WEIGHT_UNITS, label="Unit to convert from")
    to_unit = forms.ChoiceField(choices=WEIGHT_UNITS, label="Unit to convert to")


class TemperatureConverterForm(forms.Form):
    TEMPERATURE_UNITS = [
    ("c", "Celsius"),
    ("f", "Fahrenheit"),
    ("k", "Kelvin"),
    ]

    value = forms.FloatField(label='Enter the temperature to convert')
    from_unit = forms.ChoiceField(choices=TEMPERATURE_UNITS, label="Unit to convert from")
    to_unit = forms.ChoiceField(choices=TEMPERATURE_UNITS, label="Unit to convert to")