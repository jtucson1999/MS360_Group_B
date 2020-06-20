from django import forms
    
class SigmaXForm(forms.Form):
    val = forms.FloatField(help_text="What is the initial Normal stress_x value?")

class SigmaYForm(forms.Form):
    val = forms.FloatField(help_text="What is the initial Normal stress_y value?")

class TauXYForm(forms.Form):
    val = forms.FloatField(help_text="What is the initial Shear stress_xy value?")