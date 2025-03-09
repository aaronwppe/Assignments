from django.http import HttpResponse
from django.shortcuts import render

def student_grades(request):
    students = [
        {"name": "Suresh L.", "percentage": 90},
        {"name": "Amit P.", "percentage": 45},
        {"name": "Radhika E.", "percentage": 76},
        {"name": "Nidhi V.", "percentage": 39},
    ]

    for s in students:
        if s["percentage"] >= 75:
            s["grade"] = "Distinction"

        elif s["percentage"] >= 40:
            s["grade"] = "Pass Class"

        else:
            s["grade"] = "Fail"

    return render(request, "student_data.html", {"students": students})