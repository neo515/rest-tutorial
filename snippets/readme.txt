# views.py
v1 snippet_list snippet_detail  # 传统方式
v2 SnippetList  SnippetDetail   # APIView
v3 SnippetList  SnippetDetail   # generics.GenericAPIView
v4 SnippetList  SnippetDetail  UserList  UserDetail  api_root  SnippetHighlight  # generics.ListCreateAPIView
v5 SnippetViewSet    UserViewSet  api_root  # viewsets

# serializer.py
1 SnippetSerializer 
2 SnippetSerializer UserSerializer
3 SnippetSerializer UserSerializer