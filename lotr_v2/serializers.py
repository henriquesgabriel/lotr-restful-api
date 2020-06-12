from rest_framework import serializers

from .models import *


class RaceSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Race
        fields = ("identifier", "url")


class CharacterSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ("identifier", "url")


class RaceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = ("identifier", "character")


class CharacterDetailSerializer(serializers.ModelSerializer):

    race = serializers.HyperlinkedIdentityField(view_name='race-detail')

    class Meta:
        model = Character
        fields = ("id", "identifier", "height", "race", "gender", "birth",
                  "spouse", "death", "realm", "hair", "race")
