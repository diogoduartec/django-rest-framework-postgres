from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import Tag
from recipe import serialzers


class TagView(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serialzers.TagSerializer
    authentication_class = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')