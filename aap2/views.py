from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
import json
from aap2.models import CourseModel
from aap2.forms import  CourseForm
from django.core.serializers import serialize

# Create your views here.
class CourseOperation(View):

#Insert A Record
    def post(self,request):
        data=request.body
        dict_data=json.loads(data)
        # CourseModel(name=dict_data['name'],fee=dict_data['fee']).save()
        cf=CourseForm(dict_data)
        if cf.is_valid():
            cf.save()
            json_data=json.dumps({'messages':'Course is successfully Saved'})
        else:
            json_data=json.dumps({'error':cf.errors})
        return HttpResponse(json_data,content_type='application/json')

    #Reading One Record
    def get(self,request,cid=0):
        if cid==0:
            res=CourseModel.objects.all()
            json_data=serialize('json',res)
        else:
            try:
                res = CourseModel.objects.get(idno=cid)
                json_data = serialize('json', [res])
            except CourseModel.DoesNotExist:
                json_data = json.dumps({'erroe': "Invalid Id no"})
        return HttpResponse(json_data,content_type='application/json')

