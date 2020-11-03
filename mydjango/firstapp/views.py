from django.shortcuts import render
from firstapp.serializers import QuestionSerializer
from firstapp.models import Question

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


def index(request):
    """Return index template with content_data"""
    content_data = {
        "content": "Hello, Django App"
    }
    return render(request, 'index.html', context=content_data)


@api_view(['GET', 'POST'])
def question_collection(request):
    """Return question collections"""
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response({
            'data': serializer.data
        }, status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Post has been created'
            }, status.HTTP_201_CREATED)

        return Response({
            'message': 'Request is invalid'
        }, status.HTTP_400_BAD_REQUEST)

    return Response({
        'message': 'Route not found'
    },  status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'DELETE', 'PUT'])
def question_element(request, question_id):
    """Get and Manipulate question element"""
    try:
        question = Question.objects.get(id=question_id)
        print(f"question choices: {question.choices.all()}")
    except Question.DoesNotExist:
        return Response({
            'data': None
        }, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)

        return Response({
            'data': serializer.data
        }, status.HTTP_200_OK)

    if request.method == 'DELETE':
        question.delete()
        return Response({
            'message': 'Delete question success',
            'data': {
                'question_id': question_id
            }
        }, status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Update successfully',
                'data': {
                    'question_id': question_id
                }
            }, status.HTTP_200_OK)
        return Response({
            'message': 'Update not success'
        }, status.HTTP_400_BAD_REQUEST)

    return Response({
        'message': 'Route not found'
    }, status.HTTP_404_NOT_FOUND)
