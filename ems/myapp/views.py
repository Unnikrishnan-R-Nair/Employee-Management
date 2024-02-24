from django.shortcuts import render, redirect

from myapp.models import EmployeeDetails

from django.views.generic import View

from myapp.forms import EmployeeDetailsForm

# Create your views here.

# def employees_list_view(request, *args, **kwargs):

#     data = EmployeeDetails.objects.all()
    
#     return render(request, 'myapp/employee_list.html', {'data': data})


class EmployeeListView(View):
    
    def get(self, request, *args, **kwargs):

        data = EmployeeDetails.objects.all()

        return render(request, 'myapp/employee_list.html', {'data': data})
    


class EmployeeCreateView(View):

    def get(self, request, *args, **kwargs):

        form = EmployeeDetailsForm()

        return render(request, 'myapp/employee_add.html', {'form': form})
    
    
    def post(self, request, *args, **kwargs):
        
        # print(request.POST)

        form = EmployeeDetailsForm(request.POST, files=request.FILES)

        if form.is_valid():

            data = form.cleaned_data
            #print(form.cleaned_data)

            EmployeeDetails.objects.create(**data)

            return redirect('employee-list')

        return render(request, 'myapp/employee_add.html', {'form': form})
    

    
class EmployeeDetailView(View):

    def get(self, request, *args, **kwargs):

        # print(kwargs)

        pk = kwargs.get('pk')

        qs = EmployeeDetails.objects.get(id=pk)

        return render(request, 'myapp/employee_detail.html', {'emp_data': qs})



class EmployeeDeleteView(View):

    def get(self,request, *args, **kwargs):

        id = kwargs.get('pk')

        EmployeeDetails.objects.get(id=id).delete()

        return redirect('employee-list')
    


class EmployeeUpdateView(View):

    def get(self, request, *args, **kwargs):

        id = kwargs.get('pk')

        emp_object = EmployeeDetails.objects.get(id=id)

        form = EmployeeDetailsForm(instance=emp_object)

        return render(request, 'myapp/employee_edit.html', {'form': form})
    
    
    def post(self, request, *args, **kwargs):

        id = kwargs.get('pk')

        emp_object = EmployeeDetails.objects.get(id=id)

        form = EmployeeDetailsForm(request.POST, files=request.FILES, instance=emp_object)

        if form.is_valid():

            form.save()

            return redirect('employee-list')
        
        else:

            return render(request, 'myapp/employee_edit.html', {'form': form})