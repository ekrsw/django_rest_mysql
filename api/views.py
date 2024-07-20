from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ItemSerializer
from rest_framework import status


class ItemView(APIView):

    serializer_class = ItemSerializer

    def get(self, request):
        return Response({'method': 'get'})
    
    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)

        # バリデーション
        #print(serializer.is_valid(raise_exception=True))
        #print(serializer.errors)
        if serializer.is_valid(raise_exception=True):
            serializer.save() # 保存(create) or 更新(update)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)

    def put(self, request):
        return Response({'method': 'put'})

    def delete(self, request):
        return Response({'method': 'delete'})

    def patch(self, request):
        return Response({'method': 'patch'})
