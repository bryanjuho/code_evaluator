import datetime
from pprint import pprint

from allauth.account.forms import LoginForm
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from evaluator.models import Submission, Classroom, Assignment

User = get_user_model()


class GoogleSocialLoginForm(LoginForm):

    def login(self, *args, **kwargs):
        return super().login(*args, **kwargs)


class ClassForm(ModelForm):
    class Meta:
        model = Classroom
        fields = [
            'name',
            'status'
        ]


class SubmissionForm(ModelForm):
    # assignment = forms.ModelChoiceField(queryset=Assignment.objects.none())
    # user = forms.ModelChoiceField(queryset=User.objects.none())

    class Meta:
        model = Submission
        fields = [
            'description',
            'file',
            'assignment',
            'user'
        ]

    def __init__(self, *args, **kwargs):
        _assignment = kwargs.pop('assignment')
        _user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.fields['assignment'].initial = _assignment
        self.fields['assignment'].widget = forms.HiddenInput()
        self.fields['user'].initial = _user
        self.fields['user'].widget = forms.HiddenInput()
    # def clean(self):
    #     cleaned_data = super().clean()
    #     cleaned_data['assignment_id'] = self._assignment.id
    #     cleaned_data['user'] = self._user
    #     return cleaned_data


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class AssignmentForm(ModelForm):

    class Meta:
        model = Assignment
        fields = [
            'name',
            'classroom',
            'answer_code',
            'attachment',
            'test_case',
            'description',
            'due',
            'status'
        ]
        widgets = {
            'due': DatePickerInput(),
        }

        def __init__(self, *args, **kwargs):
            _classroom = kwargs.pop('classroom')
            super().__init__(*args, **kwargs)

            self.fields['classroom'].initial = _classroom
            self.fields['classroom'].widget = forms.HiddenInput()


class EditForm(ModelForm):
    # assignment = forms.ModelChoiceField(queryset=Assignment.objects.none())
    # user = forms.ModelChoiceField(queryset=User.objects.none())

    class Meta:
        model = Assignment
        fields = [
            'name',
            'test_case',
            'attachment',
            'description',
        ]


class ClassJoinForm(forms.Form):
    code = forms.CharField(label='Enter Invitation Code', max_length=7)

    user = None

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('code')

        if code:
            try:
                classroom = Classroom.objects.get(invitation_code=code)
                students = classroom.students.all()
                instructors = classroom.students.all()

                if students.filter(id=self.user.id).exists() or instructors.filter(id=self.user.id).exists():
                    self.add_error('code', 'You are already in this classroom.')
                else:
                    self.user.classrooms_students.add(classroom)
            except Classroom.DoesNotExist:
                self.add_error('code', 'Invalid invitation code')
        return cleaned_data
