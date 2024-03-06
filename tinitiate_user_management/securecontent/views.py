from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def securedata(request):
    if request.user.is_authenticated:
        # User is authenticated, perform actions accordingly
        message = f"Welcome, {request.user.username}!"
    else:
        # User is not authenticated, handle accordingly
        message = "You are not authenticated. Please log in."

    return Response({'message': message})