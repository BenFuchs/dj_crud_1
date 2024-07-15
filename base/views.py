from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def index(request):
    return Response('hello')

@api_view(['GET'])
def test(request):
    return Response({'test': 'success'})

@api_view(['GET', 'POST', 'PUT','DELETE'])
def students(request, id=-1):
    if request.method == 'GET':
        if id == -1:
            students = Student.objects.all()
        else:
            students = Student.objects.filter(id=id)

        student_info = []
        for student in students:
            student_info.append({
                'id': student.id,
                'Name': student.sName,
                'age': student.age
            })

        return Response({'students': student_info})
    if request.method == 'POST':
        Student.objects.create(sName = request.data['name'], age = request.data['age'])
        return Response({"student added": request.data['name']})
    
    if request.method == 'PUT':
        try:
            student = Student.objects.get(id=id)
            student.sName = request.data.get('name', student.sName)
            student.age = request.data.get('age', student.age)
            student.save()
            return Response({"student updated": student.id})
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)
    
    if request.method == 'DELETE':
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({"student deleted": id})
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)