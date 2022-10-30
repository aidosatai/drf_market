from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from products.tasks import send_email_celery

from rest_framework_simplejwt.tokens import RefreshToken

from account.models import CustomUser
from account.serializers import (
    CustomUserAllFieldsSerializer,
    CustomUserCreateSerializer,
    CustomUserListSerializer,
    CustomUserLoginSerializer,
)


class CustonUserViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserAllFieldsSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        permission_classes = self.permission_classes

        if self.action == 'create' or self.action == 'list' or self.action == 'login':
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'create':
            serializer_class = CustomUserCreateSerializer
        elif self.action == 'list':
            serializer_class = CustomUserListSerializer
        elif self.action == 'login':
            serializer_class = CustomUserLoginSerializer

        return serializer_class


    @action(methods=['post'], detail=False, url_path='login')
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if serializer.login_user():
            response = CustomUserListSerializer(serializer.validated_data['user']).data
            response['tokens'] = self.get_tokens_for_user(serializer.validated_data['user'])
            send_email_celery.delay()
            return Response(data=response, status=status.HTTP_200_OK)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
