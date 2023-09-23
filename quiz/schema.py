import graphene
from graphene_django import DjangoObjectType,DjangoListField
from .models import Quizzes,Category,Question,Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id','name')
    
class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id','title','category','quiz')

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title','quiz')

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('question','answer_text')

class Query(graphene.ObjectType):
    single_quiz = graphene.Field(QuizzesType, id = graphene.Int())
    all_quizzes = DjangoListField(QuizzesType)
    all_questions = DjangoListField(QuestionType)
    single_question = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_single_quiz(root,info,id):
        return Quizzes.objects.get(pk=id)
    def resolve_all_quizzes(root, info):
        return Quizzes.objects.all()
    def resolve_all_questions(root, info):
        return Question.objects.all()
    def resolve_single_question(root,info,id):
        return Question.objects.get(pk=id)
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)


    def resolve_quiz(root,info):
        return f"This is the first question"

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

class Mutation(graphene.ObjectType):
    update_category = UpdateCategoryMutation.Field()
    add_category = AddCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)