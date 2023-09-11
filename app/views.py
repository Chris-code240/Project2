from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import PersonSerializer
from .models import Person

@api_view(['POST'])
def create_view(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message":f"Person created with id: {serializer.data['id']}"},status=status.HTTP_200_OK)
    return JsonResponse({"message":str(serializer.errors),"success":False},status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PATCH','DELETE'])
def handle_person(request,id=0):

    if request.method == 'GET':
        try:
            person = Person.objects.get(id=id)
            serializer = PersonSerializer(instance=person)
        except Person.DoesNotExist:
            return HttpResponse("Person does not exist",status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
    
    if request.method == 'PATCH':
        try:
            person = Person.objects.get(id=id)
            person.name = request.data['name']
            person.save()
        except Person.DoesNotExist:
            return HttpResponse({"message":"Person does not exist"},status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({"message":f"Person with id: {person.id} updated"},status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        try:
            person = Person.objects.get(id=id)
            person.delete()
        except Person.DoesNotExist:
            return HttpResponse("Person does not exist",status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({"message":f"Person with id:{id} deleted"},status=status.HTTP_200_OK)        

    return HttpResponse(f"Handle Person {request.GET.get('user_id',id)}\n method -> {request.method}",status=status.HTTP_200_OK)

    

@api_view(['DELETE'])
def delete_view(req):
    id = req.GET.get('user_id',0)
    try:
        person = Person.objects.get(id=id)
        person.delete()
    except Person.DoesNotExist:
        return Response({"message":"Person does not exist"},status=status.HTTP_404_NOT_FOUND)
    return Response({"message":f"Person <id:{id}> deleted"},status=status.HTTP_200_OK)

# Create your views here.
