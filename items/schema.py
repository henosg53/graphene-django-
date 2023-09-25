import graphene
from graphene_django import DjangoObjectType,DjangoListField
from .models import Category, Item


class CategoryType(DjangoObjectType):
     class Meta:
        model = Category
        fields = ('id','name')

class ItemType(DjangoObjectType):
    class Meta:
        model = Item
        fields = ('id','name','description','price')

class Query(graphene.ObjectType):
    all_items = DjangoListField(ItemType)
    def resolve_all_items(root, info):
        return Item.objects.all()

class AddCategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return AddCategoryMutation(category=category)


 
class Mutation(graphene.ObjectType):
    add_category = AddCategoryMutation.Field() 


schema = graphene.Schema(query=Query, mutation=Mutation)