from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
# Create your views here.


@api_view(['POST'])
def vessel_details(request):
    return Response(data={'msg': "Saved successfully."}, status=status.HTTP_200_OK)
