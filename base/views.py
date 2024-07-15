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

# @api_view(['GET'])
# def get_students(request):
#     student_list = Student.objects.all()
#     serializer = StudentSerializer(student_list, many=True)
#     return Response({'students': serializer.data})

# def delete_student(request, student_id):
#     # Perform any necessary actions (logging, etc.) here
#     print(f"Deleting student with ID: {student_id}")
    
#     # Return a JSON response (optional)
#     return Response({'message': f'Deleted student with ID {student_id}'})

@api_view(['GET'])
def students(request, id=-1):
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