from django.shortcuts import render, get_object_or_404

from models import Entry, Category
from utils import paginate

def main(request):
    entries_per_page = 3
    num_page_links = 4

    query = ""
    category = ""
    if request.method == 'GET':
        query = request.GET.get('query', '')
        category = request.GET.get('category', '')
    if query:
        entry_list = Entry.objects.all().filter(title__icontains=query).order_by('-pub_date')
    elif category:
        entry_list = Category.objects.get(title=category).entry_set.all().order_by('-pub_date')
    else:
        entry_list = Entry.objects.all().order_by('-pub_date')

    page = request.GET.get('page')
    entries, page_list = paginate(entry_list, page, entries_per_page, num_page_links)

    return render(request, 'blog/main.html',
                  {'entries': entries,
                   'page_list': page_list,
                   'query': query,
                   'category': category,
                   'categories': Category.objects.all(),
                  })


def detail(request, entry_id, **kwargs):
    entry = get_object_or_404(Entry, id=entry_id)
    return render(request, 'blog/detail.html', {'entry': entry})


