from rest_framework import serializers

class NumberSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    language = serializers.ChoiceField(choices=[('en', 'English'), ('hi', 'Hindi')], default='en')
