from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics


class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return super().get_queryset()
