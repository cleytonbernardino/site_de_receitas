# from rest_framework.permissions import IsAuthenticated
from api.models import Recipe
from api.serializers.recipe import RecipeSerializer
from rest_framework.views import APIView, Response


class RecipeView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if not id:
            recipe = Recipe.objects.all()
            many = True
        else:
            many = False
            try:
                recipe = Recipe.objects.get(pk=id)
            except Recipe.DoesNotExist:
                return Response({'msg': 'Receita não encontrada'}, status=404)

        serializer = RecipeSerializer(recipe, many=many)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Receita salva com sucesso'}, status=201)

        return Response({"msg": "Não foi possivel salvar este item"}, status=400)  # noqa: E501

    def put(self, request, id: int):
        serializer = RecipeSerializer()
        try:
            recipe = Recipe.objects.get(pk=id)
        except Recipe.DoesNotExist:
            return Response({'msg': 'Receita não encontrada'}, status=404)

        serializer.update(recipe, request.data)
        return Response({'msg': 'Receita editada com sucesso'})

    def delete(self, request, id: int):
        try:
            Recipe.objects.get(pk=id).delete()
        except Recipe.DoesNotExist:
            return Response({'msg': 'Receita não encontrada'}, status=404)

        return Response({'msg': 'Receita apagada com sucesso'})
