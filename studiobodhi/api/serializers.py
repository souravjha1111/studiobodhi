from rest_framework import serializers
from .models import blogMOdel, urlModel, contactModel


class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogMOdel
        fields = "__all__"

class urlSerializer(serializers.ModelSerializer):
    class Meta:
        model = urlModel
        fields = "__all__"

class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactModel
        fields = "__all__"
