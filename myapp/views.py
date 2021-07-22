from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.


class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        # show list of candiadtes
        candidates = Resume.objects.all()
        return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})
        # return HttpResponseRedirect('/')

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/home.html', {'form': form})


class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate': candidate})
