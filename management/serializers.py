from rest_framework import serializers
from .models import management


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = management
        fields = ('__all__')
        # fields = ['first_name', 'last_name', 'phone']
