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
        fields = ('name','description','price','photo','category')

class Query(graphene.ObjectType):
    all_items = DjangoListField(ItemType)
    all_categories = graphene.List(CategoryType)
    single_item = graphene.Field(ItemType, id=graphene.Int())
    single_category = graphene.Field(CategoryType, id=graphene.Int())
    
    def resolve_all_items(root, info):
        return Item.objects.all()
    def resolve_all_categories(root,info):
        return Category.objects.all()
    def resolve_single_item(root,info,id):
        return Item.objects.get(pk=id)
    def resolve_single_category(root,info,id):
        return Category.objects.get(pk=id)
    
# category mutations
class AddCategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return AddCategoryMutation(category=category)

class UpdateCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id, name):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return UpdateCategoryMutation(category=category)

class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:    
        id = graphene.ID()
    
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return

# item Mutations
# needs adjustment for photos
class AddItemMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        price = graphene.Float()
        photo = graphene.String()
        category = graphene.Int(required=True)
    
    item = graphene.Field(ItemType)
    @classmethod
    def mutate(cls, root, info, name, description,price,photo,category):
        item = Item(name,description, price,photo,category)
        item.save()
        return AddItemMutation(item=item)

class UpdateItemMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    item = graphene.Field(ItemType)
    @classmethod
    def mutate(cls, root, info, name):
        item = Item.objects.get(name=name)
        return UpdateCategoryMutation(item=item)

class DeleteItemMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    item = graphene.Field(ItemType)
    @classmethod
    def mutate(cls, root, info, id):
        item = Item.objects.get(id=id)
        item.delete()
        return

class Mutation(graphene.ObjectType):
    add_category = AddCategoryMutation.Field() 
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()
    add_item = AddItemMutation.Field()
    update_item = UpdateItemMutation.Field()
    delete_item = DeleteItemMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)