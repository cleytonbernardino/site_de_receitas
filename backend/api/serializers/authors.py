from api.models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, required=False)
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=40)
    created_at = serializers.DateTimeField(required=False, read_only=True)
    updated_at = serializers.DateTimeField(required=False, read_only=True)

    def save(self):
        return Author.objects.create(**self.validated_data)

    def update(self):
        self.instance.name = self.validated_data.get(
            'name', self.instance.name
        )
        self.instance.username = self.validated_data.get(
            'username', self.instance.username
        )
        self.instance.email = self.validated_data.get(
            'email', self.instance.email
        )
        self.instance.password = self.validated_data.get(
            'password', self.instance.password
        )
        self.instance.save()
        return self.instance
