request.POST  # 只处理表单数据  只适用于'POST'方法  
request.data  # 处理任意数据  适用于'POST'，'PUT'和'PATCH'方法

from rest_framework.response import Response
return Response(serializer.data)
return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def snippet_list(request):

#### 自动给网址添加可选的格式后缀
```python
def snippet_list(request, format=None):
def snippet_detail(request, pk, format=None):

# urls.py文件，给现有的URL后面添加一组format_suffix_patterns。
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)

#访问
alias http='http -a admin:admin'
http -a admin:admin http://127.0.0.1:8000/snippets/ Accept:application/json
http                http://127.0.0.1:8000/snippets/ Accept:text/html   #注意: 这里返回的并不是json数据的字符串形式

http                http://127.0.0.1:8000/snippets.json
http                http://127.0.0.1:8000/snippets.api   #注意: 这里返回的并不是json数据的字符串形式

# 提交数据
http --form POST http://127.0.0.1:8000/snippets/ code="print 123" title='my snippet'   #测试未成功
http --debug --json POST http://127.0.0.1:8000/snippets/ code="print 456" title="test-python"
```
