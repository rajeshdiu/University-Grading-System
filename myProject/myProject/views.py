from django.shortcuts import render, redirect
from .forms import SubjectForm
from myApp.models import Student, SubjectModel

GRADE_POINTS = {
    'A+': 4.00,
    'A': 3.75,
    'A-': 3.50,
    'B+': 3.25,
    'B': 3.00,
    'B-': 2.75,
    'C+': 2.50,
    'C': 2.25,
    'D': 2.00,
    'F': 0.00,
}

def calculate_weighted_grade_point(grade, credit_hours):
    if grade in GRADE_POINTS:
        return GRADE_POINTS[grade] * credit_hours
    return 0.0


# ... (existing imports)

# ... (existing imports)

def dashboardPage(request):
    students = Student.objects.all()
    subjects = []
    selected_student = None
    show_cgpa = False
    overall_cgpa = 0.0
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            subject = form.save(commit=False)
            
            existing_subjects = SubjectModel.objects.filter(student=subject.student, name=subject.name)
            if not existing_subjects.exists():
                subject.save()

            subjects = SubjectModel.objects.filter(student=subject.student)

        elif 'selected_student' in request.POST:
            student_id = request.POST.get('selected_student')
            selected_student = Student.objects.get(id=student_id)
            subjects = SubjectModel.objects.filter(student=selected_student)

        elif 'calculate_cgpa' in request.POST and subjects:
            total_wgp = sum([subj.weighted_grade_point for subj in subjects])
            total_credit_hours = sum([subj.credit_hours for subj in subjects])

            if total_credit_hours != 0:
                overall_cgpa = total_wgp / total_credit_hours
                show_cgpa = True

    return render(request, 'dashboardPage.html', {'form': form, 'students': students, 'selected_student': selected_student, 'subjects': subjects, 'show_cgpa': show_cgpa, 'overall_cgpa': overall_cgpa})

def deleteSubject(request, myid):
    SubjectModel.objects.filter(id=myid).delete()
    return redirect('dashboardPage')
