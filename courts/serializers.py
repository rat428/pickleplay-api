from rest_framework import serializers
from .models import Court
from photos.serializers import PhotoSerializer


class CourtSerializer(serializers.ModelSerializer):
    images = PhotoSerializer(many=True)

    class Meta:
        model = Court
        fields = '__all__'


class CourtDistanceSerializer(serializers.ModelSerializer):
    images = PhotoSerializer(many=True)
    distance = serializers.SerializerMethodField()

    def get_distance(self, obj):
        return obj.distance.mi

    class Meta:
        model = Court
        fields = '__all__'
        read_only_fields = ['distance']
