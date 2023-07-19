from rest_framework import serializers
from appTienda.models import Categoria, Producto


class CategoriaSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id','catNombre')


class ProductoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id','proCodigo','proNombre','proPrecio','proCategoria','proFoto')
