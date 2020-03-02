from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from ..models import EmployeeUser
from .serializers import EmployeeUserSerializer

from ..tasks import user_added

class WidgetFilter(django_filters.FilterSet):
    class Meta:
        model = EmployeeUser
        fields = ['empno', 'name']


class EmployeeUserReadView(generics.ListAPIView):
    serializer_class = EmployeeUserSerializer
    queryset = EmployeeUser.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filter_class = WidgetFilter


class EmployeeUserCreateView(generics.CreateAPIView):
    serializer_class = EmployeeUserSerializer
    queryset = EmployeeUser.objects.all()

    def post(self, request, *args, **kwargs):
        user_added(request.data)
        return Response({"msg": 'ok'}, status=status.HTTP_200_OK)
