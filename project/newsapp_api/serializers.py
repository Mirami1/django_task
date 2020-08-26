from rest_framework import serializers

from newsapp.models import News


class NewsSerializer(serializers.Serializer):
    heading = serializers.CharField(max_length=80)
    description = serializers.CharField()
    creation_date = serializers.DateField()
    update_date = serializers.DateField()

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.heading = validated_data.get('heading', instance.heading)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.creation_date = validated_data.get(
            'creation_date', instance.creation_date)
        instance.update_date = validated_data.get(
            'update_date', instance.update_date)
        instance.save()
        return instance
