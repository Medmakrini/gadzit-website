from graphene_django import DjangoObjectType
import graphene
from .models import Formation


class FormationType(DjangoObjectType):
    class Meta:
        model = Formation


class AddFormation(graphene.Mutation):
    location = graphene.Field(FormationType)

    class Arguments:
        email=graphene.String()
        phone=graphene.String()
        first_name=graphene.String()
        last_name=graphene.String()
        choices=graphene.String()
         

    def mutate(self, info, email, phone,first_name,last_name,choices):
        f = Formation(email=email,phone=phone ,first_name=first_name, last_name=last_name,choices=choices)
        f.save()
        return AddFormation(location=f)


