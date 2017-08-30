from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import temp_read
from django.views import View


class exp(View):  

    def get(self, request, *args, **kwargs):
        
        return HttpResponse('this is a get request')

    def post(self, request, *args, **kwargs):
        
        temp = request.POST.get("temperature", "")
        obj = temp_read()
        obj.temp = temp
        obj.save()
        print('Data was sent successfully')
        return HttpResponse('DONE')


def index(request):
    latest_question_list = temp_read.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
	
