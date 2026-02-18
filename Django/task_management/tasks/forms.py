from django import forms
from tasks.models import Task

# django form
class TaskForm(forms.Form):
    title = forms.CharField(max_length=255, label="Task title")
    description = forms.CharField(widget=forms.Textarea, label="Task Description")
    # img= forms.ImageField()
    due_date= forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label='Assigned To')
    
    def __init__(self, *args, **kwargs):
        employees = kwargs.pop("employees", [])
        print(employees)
        
        super().__init__(*args, **kwargs)
        self.fields['assigned_to'].choices = [
            (emp.id, emp.name) for emp in employees]

        
    
# Django model form

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']
        # exclude= ['project', 'is_completed', 'created_at', "updated_at", ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 focus:outline-none focus:ring-2 focus:ring-rose-500',
                'placeholder': 'Enter task title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-2 h-40 focus:outline-none focus:ring-2 focus:ring-rose-500',
                'placeholder': 'Describe the task'
            }),

            'due_date': forms.SelectDateWidget(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-rose-500'
            }),

            'assigned_to': forms.CheckboxSelectMultiple(attrs={
                'class': 'h-4 w-4 text-rose-600 border-gray-300 rounded focus:ring-rose-500'
            }),
        }