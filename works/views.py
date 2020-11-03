from django.shortcuts import render

from works.models import Work

def work_overview(request):
    '''
    Retrieves all artworks from the database, which is used to
    define the context dictionary.
    ret: Renders the works overview page, passing in context with all works
    '''
    works = Work.objects.all()
    context = {
        'works': works
    }
    return render(request, 'work_overview.html', context)

def work_detail(request, pk):
    '''
    Retrieves the artwork that matches the correct primary key,
    which is used to define the context dictionary.
    args:
        pk: the primary key of the designated Work
    ret: Renders the works detail page, passing in context with a singular work
    '''
    work = Work.objects.get(pk=pk)
    context = {
        'work': work
    }
    return render(request, 'work_detail.html', context)