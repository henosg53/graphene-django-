import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery,MeQuery
# from quiz.schema import schema as quiz_schema
from items.schema import schema as item_schema


class Query(UserQuery, MeQuery, item_schema.Query, graphene.ObjectType):
    
    pass

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_mail = mutations.ResendActivationEmail.Field()
    forgotten_password = mutations.SendPasswordResetEmail.Field()

class Mutation(AuthMutation, item_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)