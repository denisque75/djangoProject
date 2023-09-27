from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ['question', 'choice_text', 'votes']


# class QuestionSerializer(serializers.HyperlinkedModelSerializer):
#     choice = serializers.SlugRelatedField(many=False, read_only=True, slug_field='choice_text')
#     class Meta:
#         model = Question
#         fields = ['question_text', 'pub_date', 'was_published_recently', 'choice']


"""
Explicit serializing 
"""
# class QuestionSerializer(serializers.Serializer):
#     question_text = serializers.CharField(required=True, allow_blank=False, max_length=180)
#     pub_date = serializers.DateTimeField()
#     was_published_recently = serializers.BooleanField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Question` instance, given the validated data.
#         """
#         return Question().objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Question` instance, given the validated data.
#         """
#         instance.question_text = validated_data.get('question_text', instance.question_text)
#         instance.pub_date = validated_data.get('pub_date', instance.pub_date)
#         instance.was_published_recently = validated_data.get('was_published_recently', instance.was_published_recently())
#         instance.save()
#         return instance


"""
Model serializing
"""
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    choice_list = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'was_published_recently', 'choice_list']
        ordering_by = 'id'
    
    def get_choice_list(self, instance: Question):
        choice_list = instance.choice_set.filter(question = 1)
        print(choice_list)
        print('\n\n\n\n\nNew Line')
        return ChoiceSerializer(choice_list, many=True, context=self.context).data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name',]
