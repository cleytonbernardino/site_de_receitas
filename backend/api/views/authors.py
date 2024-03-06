from api.models import Author
from api.serializers.authors import AuthorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response


class AuthorCreateView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'msg': 'Author cadastrado com sucesso'}, status=201
            )
        return Response(
            {'msg': 'Não foi possivel cadastrar esse author'}, status=400
        )


class AuthorsView(APIView):
    permission_classes = [IsAuthenticated]

    def get_author(self, id: int):
        try:
            return Author.objects.get(pk=id)
        except Author.DoesNotExist:
            return None

    def get(self, request, id: int):
        author = self.get_author(id)
        if author is None:
            return Response({'msg': 'Author não encontrado'}, status=404)

        serializer = AuthorSerializer(data=author)
        return Response({'msg': serializer.data})

    def put(self, request, id: int):
        author = self.get_author(id)
        if author is None:
            return Response({'msg': 'Author não encontrado'}, status=404)

        serializer = AuthorSerializer(instance=author, data=request.data)
        if serializer.is_valid():
            serializer.update()
        return Response({'msg': 'Author atualizado com sucesso'})

    def delete(self, request, id: int):
        author = self.get_author(id)
        if author is None:
            return Response({'msg': 'Author não encontrado'}, status=404)

        author.delete()
        return Response({'msg': 'Author apagado com sucesso'})
