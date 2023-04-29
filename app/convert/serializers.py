from rest_framework import serializers


class CropSerializer(serializers.Serializer):
    x = serializers.FloatField()
    y = serializers.FloatField()
    width = serializers.FloatField()
    height = serializers.FloatField()


class ConvertSerializer(serializers.Serializer):
    base64data = serializers.CharField(min_length=1)
    convertDirection = serializers.ChoiceField(choices=['a2b', 'b2a'])
    crop = CropSerializer()
    model = serializers.ChoiceField(choices=['chipndale', 'mickey'])

    class Meta:
        fields = ["base64data", "convertDirection", "crop", "model"]

