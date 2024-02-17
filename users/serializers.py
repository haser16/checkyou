from rest_framework import serializers

from .models import Questions, Tests


class TestsSerializer(serializers.ModelSerializer):
    number_class = serializers.SlugRelatedField(slug_field='name', read_only=True)
    teacher = serializers.SlugRelatedField(slug_field='name', read_only=True)
    subject = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Tests
        fields = ('id', 'school', 'name', 'number_class', 'teacher', 'subject', 'image')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('test', 'question', 'answer1', 'answer2', 'answer3')
