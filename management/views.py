from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import management
from .serializers import ContactSerializer

# Create your views here.


def hello(request):
    return HttpResponse('Got It')


class ContactView(ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        queryset = management.objects.all()
        phonenumber = self.request.query_params.get('phone')
        name = self.request.query_params.get('name')
        if phonenumber is not None:
            queryset = queryset.filter(phone__startswith=phonenumber)
        if name is not None:
            queryset = queryset.filter(first_name__istartswith=name)
        return queryset


class ContactViewDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = management.objects.all()
