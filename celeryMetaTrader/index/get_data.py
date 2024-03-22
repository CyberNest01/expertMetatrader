from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST'])
def get_meta_data(request):
    print(request.data)
    return Response({'message': 'done'}, status=status.HTTP_200_OK)
