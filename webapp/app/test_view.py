from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request):
        return render(request, 'index.html', {'page': 'index'})
    def post(self, request):
        data = {
            'userId': 'dooho',
            'name': '함두호'
        }
        return JsonResponse(data)