from api.models import Recipe
from rest_framework import serializers


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=40)
    preparation_time = serializers.IntegerField()
    preparation_unit = serializers.CharField(max_length=20)
    servings = serializers.IntegerField()
    servings_unit = serializers.CharField(max_length=20)
    is_html = serializers.BooleanField(default=False)
    preparation_steps = serializers.CharField()
    cover = serializers.ImageField(required=False)

    def save(self):
        return Recipe.objects.create(**self.validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.preparation_time = validated_data.get(
            'preparation_time', instance.preparation_time
        )
        instance.preparation_unit = validated_data.get(
            'preparation_unit', instance.preparation_unit
        )
        instance.servings = validated_data.get('servings', instance.servings)
        instance.servings_unit = validated_data.get(
            'servings_unit', instance.servings_unit
        )
        instance.is_html = validated_data.get('is_html', instance.is_html)
        instance.preparation_steps = validated_data.get(
            'preparation_steps', instance.preparation_steps
        )
        instance.cover = validated_data.get('cover', instance.cover)
        instance.save()
        return instance
