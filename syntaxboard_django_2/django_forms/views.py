from django.shortcuts import render, HttpResponse
from django.template import loader
from .forms import TrainingForm

def simple_form(request):
    
    if request.method == 'POST':

        # Create Template Object
        template = loader.get_template('django_forms_output.html')
        ObjForm = TrainingForm(request.POST)

        if ObjForm.is_valid():

            # Get the Choice Position of the selected values from post
            drop_down_data = ObjForm.cleaned_data.get('DropDownBox')
            radio_data = ObjForm.cleaned_data['RadioButtons']
            multi_data_list = ObjForm.cleaned_data['MultiSelect']
            checkbox_data_list = ObjForm.cleaned_data['CheckBox']
            print(multi_data_list)
            
            # print(ObjForm.form_choices[int(drop_down_data)-1])
            # Single Selected Choice
            dd_var = ObjForm.form_choices[int(drop_down_data)-1][1]
            rd_var = ObjForm.form_choices[int(radio_data)-1][1]

            # Multi Selected Choice
            md_list = []
            for i in multi_data_list:
                md_list.append(ObjForm.form_choices[int(i)-1][1])

            # Check Box Selected Choice    
            cd_list = []
            for i in checkbox_data_list:
                cd_list.append(ObjForm.form_choices[int(i)-1][1])
            
            # UserID and Password Text Box values
            userid_txt = ObjForm['userid'].value()
            passwd_txt = ObjForm['passwd'].value()
            date_data  = ObjForm.cleaned_data['dateinput']
                
        # Data (context) to be passed to template
        context = {
            'user_id': userid_txt,
            'pass_wd': passwd_txt,
            'date_data': date_data,
            'DropDown_data' : dd_var,
            'Radio_Selected' : rd_var,
            'MultiList_Selected' : md_list,
            'CheckBox_Selected' : cd_list,
        }

        # Use the "context" to render the HTML Template to display values
        return HttpResponse(template.render(context, request))

    else:
        form = TrainingForm
        return render(request,'django_forms_input.html',{'form':form})
