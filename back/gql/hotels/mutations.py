from graphene import Boolean, Field, ID, InputObjectType, Mutation, String
from rest_framework import serializers
from hotels.models import Hotel
from .types import HotelType


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = (
            'id',
            'title',
            'body',
        )


class HotelInputType(InputObjectType):
    title = String()
    body = String()


class HotelCreate(Mutation):
    class Arguments:
        input = HotelInputType(required=True)

    hotel = Field(HotelType)

    @classmethod
    def mutate(cls, root, info, **data):
        serializer = HotelSerializer(data=data.get('input'))
        serializer.is_valid(raise_exception=True)

        return HotelCreate(hotel=serializer.save())


class HotelDelete(Mutation):
    class Arguments:
        id = ID(required=True)

    ok = Boolean()

    @classmethod
    def mutate(cls, root, info, **data):
        hotel = Hotel.objects.get(id=data.get('id'))
        hotel.delete()

        return HotelDelete(ok=True)