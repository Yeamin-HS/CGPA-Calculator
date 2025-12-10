from django.shortcuts import render
from .forms import CGPAForm

def calculate_cgpa(completed_courses, current_cgpa, grades):
    credit_per_course = 3
    total_completed_credits = completed_courses * credit_per_course
    total_completed_points = current_cgpa * total_completed_credits

    new_credits = len(grades) * credit_per_course
    new_points = sum([float(g) * credit_per_course for g in grades])

    total_points = total_completed_points + new_points
    total_credits = total_completed_credits + new_credits

    return round(total_points / total_credits, 2) if total_credits > 0 else 0.0

def cgpa_counter(request):
    cgpa = None
    form = CGPAForm(request.POST or None)

    if request.method == "POST":
        new_courses = int(request.POST.get("new_courses", 0))
        form = CGPAForm(request.POST, extra=new_courses)

        if form.is_valid():
            completed = form.cleaned_data["completed_courses"]
            current = form.cleaned_data["current_cgpa"]
            grades = [form.cleaned_data[f"course_{i+1}"] for i in range(new_courses)]
            cgpa = calculate_cgpa(completed, current, grades)
    else:
        form = CGPAForm()

    return render(request, "grades/cgpa_counter.html", {"form": form, "cgpa": cgpa})
