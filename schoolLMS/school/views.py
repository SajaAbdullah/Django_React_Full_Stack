from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from school.models import Teacher
from school.serializers import UserSerializer


class TeacherListGenaricView(generics.ListAPIView):
    """
    using genaric views list teachers
    """
    queryset = Teacher.objects.all()
    serializer_class = UserSerializer

class TeacherRetrieveGenaricView(generics.RetrieveAPIView):
    """
    using genaric RetrieveAPIView retrive teacher
    """
    queryset = Teacher.objects.all()
    serializer_class = UserSerializer
    lookup_field="id"
   