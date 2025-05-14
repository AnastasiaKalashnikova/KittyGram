from rest_framework import serializers # type: ignore


from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('name', 'color', 'birth_year')
