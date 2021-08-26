from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import DraftResultForm, ImportResultsForm
from .models import DraftResult
from .services.excel_file_handler import excelFileHandler

def index(request):
    return render(request, 'MTG_Tracker/index.html')

@login_required
def myResults(request):
    user = request.user
    draft_results = DraftResult.objects.filter(user=user).order_by('-date')
    return render(request, 'MTG_Tracker/myresults.html', {'draft_results': draft_results})

@login_required
def addResult(request):
    user = request.user
    draft_results = DraftResult.objects.filter(user=user).order_by('-date')
    if request.method == 'POST':
        new_draft_result = DraftResult(user=user)
        form = DraftResultForm(request.POST, instance=new_draft_result)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/myresults/add_new_result')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DraftResultForm()
    return render(request, 'MTG_Tracker/add_new_results.html', {'form': form, 'draft_results': draft_results})

@login_required
def importResults(request):
    user = request.user
    draft_results = DraftResult.objects.filter(user=user).order_by('-date')
    if request.method == 'POST':
        form = ImportResultsForm(request.POST, request.FILES)
        if form.is_valid():
            new_draft_results = excelFileHandler(request.FILES['file'], user)
            if len(new_draft_results) == 0:
                return render(request, 'MTG_Tracker/import_results.html', {'form': form, 'draft_results': draft_results, 'excel_error': "les données ne sont pas valides !"})
            for new_draft_result in new_draft_results:
                new_draft_result.save()
            return HttpResponseRedirect('/myresults/import_results')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ImportResultsForm()
    return render(request, 'MTG_Tracker/import_results.html', {'form': form, 'draft_results': draft_results})

@login_required
def updateDraftResult(request, draft_result_id):
    user = request.user
    dr = DraftResult.objects.get(id=draft_result_id)
    if dr.user != user:
        return HttpResponseRedirect('/myresults')
    if request.method == 'POST':
        form = DraftResultForm(request.POST, instance=dr)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/myresults')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DraftResultForm(instance=dr)
    return render(request, 'MTG_Tracker/update_result.html', {'form': form})
    
@login_required
def deleteDraftResult(request, draft_result_id):
    user = request.user
    dr = DraftResult.objects.get(id=draft_result_id)
    if dr.user == user:
        dr.delete()
    return HttpResponseRedirect('/myresults')