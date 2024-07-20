from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
import pika
from django.conf import settings
import json 
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Publish UserRegistered event
            connection = pika.BlockingConnection(pika.URLParameters(settings.RABBITMQ_URL))
            channel = connection.channel()
            event = {
                'type': 'UserRegistered',
                'data': {
                    'username': request.data['username'],
                    'email': request.data['email']
                }
            }
            channel.basic_publish(exchange='', routing_key='user-events', body=json.dumps(event))
            connection.close()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetRequestView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            # Simulate password reset request handling
            # Publish PasswordResetRequested event
            connection = pika.BlockingConnection(pika.URLParameters(settings.RABBITMQ_URL))
            channel = connection.channel()
            event = {
                'type': 'PasswordResetRequested',
                'data': {'email': email}
            }
            channel.basic_publish(exchange='', routing_key='user-events', body=json.dumps(event))
            connection.close()
            return Response({'message': 'Password reset requested'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
