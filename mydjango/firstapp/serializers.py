"""Rest framework for Django"""
from rest_framework import serializers
from firstapp.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializes Choice model to return in JSON"""

    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class QuestionSerializer(serializers.ModelSerializer):
    """Serializes Question model to return in JSON"""
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'published_date', 'choices')

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question

    def update(self, instance, validated_data):
        instance.question_text = validated_data.get(
            'question_text', instance.question_text)
        instance.published_date = validated_data.get(
            'published_date', instance.published_date)
        instance.save()

        choices_data = validated_data.pop('choices')
        choices = (instance.choices).all()
        choices = list(choices)
        for choice_data in choices_data:
            choice = choices.pop(0)
            choice.choice_text = choice_data.get(
                'choice_text', choice.choice_text)
            choice.votes = choice_data.get('votes', choice.votes)
            choice.save()

        return instance
