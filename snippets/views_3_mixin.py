from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)  # mixin类提供.list()和.create()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  # mixin类提供.list()和.create()

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  # mixins来提供.retrieve()），.update()和.destroy()操作。

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)    # mixins来提供.retrieve()），.update()和.destroy()操作。

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)   # mixins来提供.retrieve()），.update()和.destroy()操作。