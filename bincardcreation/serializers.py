from rest_framework import serializers
from bincardcreation.models import Material

class Materialserializers(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = '__all__'