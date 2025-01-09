from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from .calculation.base import calculate_promp_input
from .models import PrompMainAi
from .serializers import PrompMainAiSerializer


class ConstructionProjectView(APIView):
    
    def post(self, request, slug_promp):
        text_user_data = request.data.get("prompt")
    
        promp_main_instance = PrompMainAi.objects.get(slug_promp=slug_promp)

        print(text_user_data)
        promp_main = promp_main_instance.promp_main

        responseAPI = calculate_promp_input(promp_main,text_user_data, slug_promp)
        print(responseAPI)
        if "error" in responseAPI:
            return Response(responseAPI, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(responseAPI, status=status.HTTP_200_OK)


class TypeProyectViewList(ListAPIView):
    queryset = PrompMainAi.objects.all()
    serializer_class = PrompMainAiSerializer


class ProyectDetailView(RetrieveAPIView):
    serializer_class = PrompMainAiSerializer
    lookup_field = 'slug_promp'
    queryset = PrompMainAi.objects.filter()
