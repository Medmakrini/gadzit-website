import graphene
from graphene_django import DjangoObjectType
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
import graphql_jwt

from django.contrib.auth.hashers import make_password

from users.models import ExtendUser
from FormationForm.models import Formation as FM
from FormationForm.schema import (
    FormationType,
    AddFormation,

)

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()
   resend_activation_email = mutations.ResendActivationEmail.Field()
   send_password_reset_email = mutations.SendPasswordResetEmail.Field()
   password_reset = mutations.PasswordReset.Field()
   password_change = mutations.PasswordChange.Field()
   verify_token = graphql_jwt.Verify.Field()
   refresh_token = graphql_jwt.Refresh.Field()
   revoke_token = graphql_jwt.Revoke.Field()


class DeletUser(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        id = graphene.ID()
    def mutate(cls, info, **kwargs):
        obj = ExtendUser.objects.get(pk=kwargs["id"])
        obj.delete()
        return DeletUser(ok=True)


class VerifyUser(graphene.Mutation):
    ok = graphene.Boolean()
    class Arguments:
        id = graphene.ID()
    def mutate(cls, info, **kwargs):
        obj = ExtendUser.objects.get(pk=kwargs["id"])
        obj.status.verified=True
        obj.is_active=True
        obj.status.save()
        obj.save()

        return VerifyUser(ok=True)



class VerifyAuth(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        phone = graphene.String()

    def mutate(cls, info, phone):
        obj = ExtendUser.objects.get(phone=phone)
        obj.status.verified=True
        obj.is_active=True
        obj.status.save()
        obj.save()

        return VerifyAuth(ok=True)


class ChangePass(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        phone = graphene.String()
        password = graphene.String()

    def mutate(cls, info, phone,password):
        obj = ExtendUser.objects.get(phone=phone)
        encryptedpassword=make_password(password)
        obj.password=encryptedpassword
        obj.save()
        return ChangePass(ok=True)
        

class IsUserExist(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        phone = graphene.String()

    def mutate(cls, info, phone):
        obj = ExtendUser.objects.get(phone=phone)
        if(obj):
            return IsUserExist(ok=True)
        else:
            return IsUserExist(ok=False)


class BlockUser(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    def mutate(cls, info, **kwargs):
        obj = ExtendUser.objects.get(pk=kwargs["id"])
        obj.status.verified=False
        obj.is_active=False
        obj.status.save()
        obj.save()
        return BlockUser(ok=True)

class UpdateAccount(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()
        phone=graphene.String()
        first_name=graphene.String()
        last_name=graphene.String()
        email=graphene.String()
    def mutate(cls, info,phone,first_name,last_name,email, **kwargs):
        obj = ExtendUser.objects.get(pk=kwargs["id"])
        obj.phone=phone
        obj.first_name=first_name
        obj.last_name=last_name
        obj.email=email
        obj.save()
        return UpdateAccount(ok=True)


class Query(UserQuery, MeQuery, graphene.ObjectType):
     farms=graphene.List(FormationType)

     def resolve_farms(self,info):
         return FM.objects.all()

    

class Mutation(AuthMutation, graphene.ObjectType):
    Add_Formation = AddFormation.Field()
    Update_Account=UpdateAccount.Field()
    Delet_user=DeletUser.Field()
    Verify_User=VerifyUser.Field()
    Verify_Auth=VerifyAuth.Field()
    Block_user=BlockUser.Field()
    Change_Pass=ChangePass.Field()
    IsUser_Exist=IsUserExist.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)