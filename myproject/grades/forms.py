from django import forms

GRADE_CHOICES = [
    (4.0, "A (4.0)"),
    (3.7, "A- (3.7)"),
    (3.3, "B+ (3.3)"),
    (3.0, "B (3.0)"),
    (2.7, "B- (2.7)"),
    (2.3, "C+ (2.3)"),
    (2.0, "C (2.0)"),
    (1.7, "C- (1.7)"),
    (1.3, "D+ (1.3)"),
    (1.0, "D (1.0)"),
    (0.0, "F (0.0)"),
]

class CGPAForm(forms.Form):
    completed_courses = forms.IntegerField(min_value=0, label="Completed Course Count")
    current_cgpa = forms.FloatField(min_value=0.0, max_value=4.0, label="Current CGPA")
    new_courses = forms.IntegerField(min_value=1, label="Number of Courses Taken")

    def __init__(self, *args, **kwargs):
        extra_courses = kwargs.pop("extra", 0)
        super().__init__(*args, **kwargs)
        for i in range(extra_courses):
            self.fields[f"course_{i+1}"] = forms.ChoiceField(
                choices=GRADE_CHOICES, label=f"Course {i+1} Grade"
            )
