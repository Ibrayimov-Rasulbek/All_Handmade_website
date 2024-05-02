from django import forms
from .models import Mahsulot
class OrderForm(forms.ModelForm):
    class Meta:
        model=Mahsulot
        fields=['mahsulot_nomi','mahsulot_izohi','rasm','mahsulot_narxi']