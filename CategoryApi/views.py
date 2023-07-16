from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import categorySerializer
from .models import category


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/foodcategory/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of foodcategory'
        },
        {
            'Endpoint': '/foodcategory/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single foodcategory item'
        },
        {
            'Endpoint': '/foodcategory/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new foodcategory item'
        },
        {
            'Endpoint': '/foodcategory/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Update the foodcategory item'
        },
        {
            'Endpoint': '/foodcategory/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes the foodcategory item'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getCategories(request):
    categorys = category.objects.all()
    serializer = categorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategorybyId(request, pk):
    categorybyId = category.objects.get(id=pk)
    serializer = categorySerializer(categorybyId, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def creatCategory(request):
    data = request.data

    newCategory = category.objects.create(
        cat_name=data['cat_name'],
        cat_image=data['cat_image'],
        cat_desc=data['cat_desc']
    )
    serializer = categorySerializer(newCategory, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateCategory(request, pk):
    data = request.data

    categoryUpdate = category.objects.get(id=pk)
    serializer = categorySerializer(categoryUpdate, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCategory(request, pk):
    categoryDelete = category.objects.get(id=pk)
    categoryDelete.delete()
    return Response('category successfully deleted!')
