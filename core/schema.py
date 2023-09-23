import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery,MeQuery


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_mail = mutations.ResendActivationEmail.Field()
    forgotten_password = mutations.SendPasswordResetEmail.Field()

class Mutation(AuthMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)