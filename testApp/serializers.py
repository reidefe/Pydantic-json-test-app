from rest_framework import serializers
from .models import Actor, Film


class JSONSerializerField(serializers.Field):
    """"" serializer for JSONField 
            required to make field writable""" ""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class ActorSerializers(serializers.ModelSerializer):
    # data = serializers.SerializerMethodField('clean_json')
    # data = serializers.JSONField()
    data = JSONSerializerField()

    class Meta:
        model = Actor
        fields = ["name", "data"]

    def clean_json(self, obj):
        obj.json


class FilmSerializers(serializers.ModelSerializer):
    # data = serializers.SerializerMethodField('clean_json')
    data = JSONSerializerField()

    class Meta:
        model = Film
        fields = ["title", "actor", "year", "duration", "data"]

    def clean_json(self, obj):
        obj.json
