from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    body = serializers.CharField()
    url_image = serializers.CharField()
    created_date = serializers.DateTimeField()