from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .calculation.base import calculate_promp_input


class ConstructionProjectView(APIView):
    def post(self, request):
        text_user_data = request.data.get("prompt")
        print(text_user_data)

        responseAPI = calculate_promp_input(text_user_data)
        print(responseAPI)
        if "error" in responseAPI:
            return Response(responseAPI, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(responseAPI, status=status.HTTP_200_OK)




