from rest_framework.views import APIView, Response


class Recipe(APIView):
    
    def get(self, request):
        return Response({"OLÀ": "quem sou eu"})