
from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from books.models import Book, Publishing_company
from books.serializers import BookSerializer, CompanySerializer
from accounts.permissions import IsUserStaff
from rest_framework_simplejwt.authentication import JWTAuthentication

class BookView(generics.ListCreateAPIView):    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserStaff]
    queryset= Book.objects.all()
    serializer_class= BookSerializer

       
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserStaff]
    queryset= Book.objects.all()
    serializer_class= BookSerializer



class PublishCompanyView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ IsUserStaff]
    queryset= Publishing_company.objects.all()
    serializer_class= CompanySerializer
  
    def post(self, request:Request) -> Response:
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
    

class PublishCompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserStaff]

    queryset= Publishing_company.objects.all()
    serializer_class= CompanySerializer    
