from django import forms 
from produtos.models import Produtos, TipoProduto



class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TipoProduto
        fields = '__all__'


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = '__all__'