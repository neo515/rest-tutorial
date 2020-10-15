from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# 重写SnippetSerializer
# 添加了一个新的'highlight'字段。
# 该字段与url字段的类型相同，不同之处在于它指向'snippet-highlight'url模式，而不是'snippet-detail'url模式。
# 因为我们已经包含了格式后缀的URL，例如'.json'，我们还需要在highlight字段上指出任何格式后缀的超链接，它应该使用'.html'后缀。
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.CharField(source='owner.username',read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')


    class Meta:
        model = Snippet 
        # fields = (     'id',              'title', 'code', 'linenos', 'language', 'style','owner')
        fields = ('url', 'id', 'highlight', 'owner','title', 'code', 'linenos', 'language', 'style')

        # created = models.DateTimeField(auto_now_add=True)
        # title = models.CharField(max_length=100, blank=True, default='')
        # code = models.TextField()
        # linenos = models.BooleanField(default=False)
        # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
        # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
        # owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
        # highlighted = models.TextField()


from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')