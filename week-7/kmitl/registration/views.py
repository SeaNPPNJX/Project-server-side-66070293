from django.shortcuts import render, HttpResponse, redirect
from django.db.models import F, Q, Count, Value as V, OuterRef, Subquery, Sum
from django.db.models.functions import Now, Concat
from .models import *
from django.views import View

def index(request):
    student_list = Student.objects.all().order_by('student_id')
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    if search != None:
        if filter == 'email':
            student_list = Student.objects.filter(studentprofile__email__icontains=search)
        elif filter == 'faculty':
            student_list = Student.objects.filter(faculty__name__icontains=search)
        else:
            student_list = Student.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name')).filter(full_name__icontains=search)
    else:
        search = ''
    context = { 'student_list' : student_list, 'total' : student_list.count, 'search' : search, 'filter': filter}
    return render(request, 'index.html', context)

def professor(request):
    professor_list = Professor.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name'))
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    if search != None:
        if filter == 'faculty':
            professor_list = Professor.objects.filter(faculty__name__icontains=search)   
        else:
            professor_list = Professor.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name')).filter(full_name__icontains=search)
    else:
        search = ''
    context = { 'professor_list': professor_list, 'total': professor_list.count, 'search' : search, 'filter': filter}
    return render(request, 'professor.html', context)

def faculty(request):
    faculty_list = Faculty.objects.all()
    search = request.GET.get('search')
    if search != None:
        faculty_list = Faculty.objects.filter(name__icontains=search)   
    else:
        search = ''
    context = { 'faculty_list' : faculty_list, 'total' : faculty_list.count, 'search' : search}
    return render(request, 'faculty.html', context)

def course(request):
    course_list = Course.objects.all()
    search = request.GET.get('search')
    if search != None:
        course_list = Course.objects.filter(course_name__icontains=search)   
    else:
        search = ''
    context = { 'course_list' : course_list, 'total' : course_list.count, 'search' : search}
    return render(request, 'course.html', context)

class CreateStudent(View):
    def get(self, request):
        context = { 'faculties': Faculty.objects.all(), 'sections': Section.objects.all()}
        return render(request, 'create_student.html', context)
    def post(self, request):
        student_id = request.POST.get('student_id')
        faculty = request.POST.get('faculty')
        fac = Faculty.objects.get(id=faculty)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        section = request.POST.getlist('section_ids')
        new_student = Student.objects.create(student_id=student_id, first_name=first_name, last_name=last_name, faculty=fac)
        StudentProfile.objects.create(student=new_student, email=email, phone_number=phone_number, address=address)
        for i in section:
            sec = Section.objects.get(id=i)
            new_student.enrolled_sections.add(sec)
        new_student.save()
        return redirect('/')