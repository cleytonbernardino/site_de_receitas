from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=40)
    preparation_time = serializers.IntegerField()
    prepartaion_unit = serializers.CharField(max_length=20)
    servings = serializers.IntegerField()
    servings_unit = serializers.CharField(max_length=20)
    is_html = serializers.BooleanField(default=False)
    preparation_steps = serializers.CharField()
    cover = serializers.ImageField(required=False)

    def save(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        return instance
