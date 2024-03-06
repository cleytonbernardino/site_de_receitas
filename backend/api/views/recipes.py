from api.serializers import RecipeSerializer
# from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response


class Recipe(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"OLÀ": "quem sou eu"})

    def post(self, request):
        serializer = RecipeSerializer(data=request.data or '')
        if serializer.is_valid():
            serializer.save(serializer.validated_data)
            return Response({'msg': 'Receita salva com sucesso'}, status=201)

        return Response({"msg": "Não foi possivel salvar esté item"}, status=400)  # noqa: E501
