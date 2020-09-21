# back/gql/schema.py
from graphene import Argument, Field, ID, ObjectType, Schema
from graphene_django import DjangoConnectionField
from hotels.models import Hotel
from .hotels.filters import HotelFilter
from .hotels.mutations import HotelCreate, HotelDelete
from .hotels.types import HotelType

class Query(ObjectType):
    hotels = DjangoConnectionField(HotelType)
    Hotel = Field(HotelType, id=Argument(ID, required=True))
    def resolve_Hotels(root, info, **kwargs):
        return Hotel.objects.all()
    def resolve_Hotel(root, info, **kwargs):
        return Hotel.objects.get(id=kwargs.get('id'))

class Mutation(ObjectType):
    Hotel_create = HotelCreate.Field()
    Hotel_delete = HotelDelete.Field()

schema = Schema(query=Query, mutation=Mutation)