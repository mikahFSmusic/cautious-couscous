# back/gql/notes/types.py
from graphene_django import DjangoObjectType
from hotels.models import Hotel

class HotelType(DjangoObjectType):
    class Meta:
        model = Hotel
        only_fields = (
            'id',
            'title',
            'body',
            'created_at',
        )
        use_connection = True