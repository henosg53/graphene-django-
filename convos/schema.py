import graphene
from graphene_django import DjangoObjectType,DjangoListField
from .models import Conversation, ConversationMessage

class ConversationType(DjangoObjectType):
    class Meta:
        model = Conversation
        fields = ('__all__')

class ConversationMessageType(DjangoObjectType):
    class Meta:
        model = ConversationMessage
        fields = ('__all__')

class Query(graphene.ObjectType):
    all_conversations = DjangoListField(ConversationType)
    all_messages = DjangoListField(ConversationMessageType)
    single_conversation = graphene.Field(ConversationType, id=graphene.Int())
    single_message = graphene.Field(ConversationMessageType, id=graphene.Int())

    def resolve_all_conversations(root, info):
        return Conversation.objects.all()
    def resolve_all_messages(root, info):
        return ConversationMessage.objects.all()
    def resolve_single_conversation(root, info,id):
        return Conversation.objects.get(pk=id)
    def resolve_single_message(root, info):
        return ConversationMessage.objects.filter(pk=id)

# Convo msg mutations
class AddMessageMutation(graphene.Mutation):
    class Arguments:
        conversation = graphene.Int()
        content = graphene.String()
    
    conversation_message = graphene.Field(ConversationMessageType)
    @classmethod
    def mutate(cls,root,info,conversation, content):
        conversation_message = ConversationMessageType(conversation,content)
        conversation_message.save()
        return AddMessageMutation(conversation_message)
    
class UpdateMessageMutation(graphene.Mutation):
    class Arguments:
        conversation = graphene.Int()
        content = graphene.String()
    
    message = graphene.Field(ConversationMessageType)
    @classmethod
    def mutate(cls,root,info,conversation, content):
        message = ConversationMessageType(conversation,content)
        message.save()
        return AddMessageMutation(message)
    
class DeleteMessageMutation(graphene.Mutation):
    class Arguments:
        conversation = graphene.Int()
        content = graphene.String()
    
    message = graphene.Field(ConversationMessageType)
    @classmethod
    def mutate(cls,root,info,conversation, content):
        message = ConversationMessageType(conversation,content)
        message.save()
        return AddMessageMutation(message)


# convos mutations
class AddConversationMutation(graphene.Mutation):
    class Arguments:
        item = graphene.Int()

    convo = graphene.Field(ConversationType)

    @classmethod
    def mutate(cls,root,info,item):
        convo = Conversation(item=item)
        convo.save()
        return AddConversationMutation(convo)

class UpdateConversationMutation(graphene.Mutation):
    class Arguments:
        item = graphene.Int()

    convo = graphene.Field(ConversationType)

    @classmethod
    def mutate(cls,root,info,item):
        convo = Conversation(item=item)
        convo.save()
        return AddConversationMutation(convo)
  
class DeleteConversationMutation(graphene.Mutation):
    class Arguments:
        item = graphene.Int()

    convo = graphene.Field(ConversationType)

    @classmethod
    def mutate(cls,root,info,item):
        convo = Conversation(item=item)
        convo.save()
        return AddConversationMutation(convo)
  
 
class Mutation(graphene.ObjectType):
    add_message = AddMessageMutation.Field()
    update_message = UpdateMessageMutation.Field()
    delete_message = DeleteMessageMutation.Field()
    add_convo = AddConversationMutation.Field()
    update_convo = UpdateConversationMutation.Field()
    delete_convo = DeleteConversationMutation.Field()


schema =schema = graphene.Schema(query=Query, mutation=Mutation)