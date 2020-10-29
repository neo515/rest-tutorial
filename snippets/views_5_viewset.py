from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import generics

from rest_framework import permissions

from rest_framework import renderers
from rest_framework.response import Response



from rest_framework import viewsets
from snippets.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import action
from rest_framework.decorators import api_view, renderer_classes
# from rest_framework.decorators import detail_route

# 替换SnippetList，SnippetDetail和SnippetHighlight视图类
class SnippetViewSet(viewsets.ModelViewSet):
    """
    此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。

    另外我们还提供了一个额外的`highlight`操作。
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @action(detail=True)
    # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    @renderer_classes([renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# from rest_framework.decorators import detail_route

from django.contrib.auth.models import User


from rest_framework import viewsets

# 我们将UserList和UserDetail视图重构为一个UserViewSet
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    此视图自动提供`list`和`detail`操作。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })
