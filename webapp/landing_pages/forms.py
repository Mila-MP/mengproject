from django import forms
from .models import InstrumentType, Oven, Mixer


class InstrumentTypeModelForm(forms.ModelForm):
    class Meta:
        model = InstrumentType
        fields = ["instrument_type_name"]
        labels = {"instrument_type_name": "Name"}


class OvenModelForm(forms.ModelForm):
    class Meta:
        model = Oven
        fields = [
            "instrument_type",
            "instrument_name",
            "max_temp",
            "max_dim_W",
            "max_dim_L",
            "max_dim_H",
            "max_capacity",
        ]
        labels = {
            "instrument_type_name": "Instrument type",
            "instrument_name": "Oven name",
            "max_temp": "Maximum temperature",
            "max_dim_W": "Maximum tray width",
            "max_dim_L": "Maximum tray length",
            "max_dim_H": "Maximum tray height",
            "max_capacity": "Maximum oven capacity",
        }


class MixerModelForm(forms.ModelForm):
    class Meta:
        model = Mixer
        fields = ["instrument_type", "instrument_name", "max_speed", "min_speed"]
        labels = {
            "instrument_type_name": "Instrument type",
            "instrument_name": "Mixer name",
            "max_speed": "Maximum rotation speed (RPM)",
            "min_speed": "Minimum rotation speed (RPM)",
        }


action_choices = {"Mix": "Mix", "Bake": "Bake", "Proof": "Proof", "Chill": "Chill"}


class ActionForm(forms.Form):
    action_type = forms.ChoiceField(choices=action_choices)
