from django.shortcuts import render
from rest_framework import viewsets, generics, status

from .models import Court
from .serializers import CourtSerializer, CourtDistanceSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry, Point

METERS_TO_MILES_CONSTANT = 0.00621371


class CourtList(generics.ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class CourtDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


@api_view(['GET'])
def get_nearest_courts(request):
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)
    radius = request.GET.get('radius', 50)

    if lat and lng:
        user_location = Point(float(lng), float(lat), srid=4326)
        results = Court.objects.filter(location__distance_lte=(user_location, D(mi=radius)))\
            .annotate(distance=Distance("location", user_location))\
            .order_by("distance")

        serializer = CourtDistanceSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def generate_courts(request):
    """
    Generate fake courts
    """
    if request.method == 'GET':
        courts = []
        for x in range(100):
            courts.append(Court.generate_random())
        serializer = CourtSerializer(courts, many=True)
        return Response(serializer.data)




