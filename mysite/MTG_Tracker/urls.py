from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myresults/', views.myResults, name='my_results'),
    path('myresults/add_new_result', views.addResult, name='add_new_result'),
    path('myresults/import_results', views.importResults, name='import_results'),
    path('myresults/update/<int:draft_result_id>', views.updateDraftResult, name='update_result'),
    path('myresults/delete/<int:draft_result_id>', views.deleteDraftResult, name='delete_result')
]