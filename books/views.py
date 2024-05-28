from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm, AuthorSearchForm, CategorySearchForm
from .import utils
# Create your views here.


def index(request):
  return render (request,"base.html")



def title_search(request):
  if request.method == "GET":
    form=SearchForm()
    return render(request,"books/search.html", {"form":form,})
  
  if request.method == "POST":
    form=SearchForm(request.POST)
    if form.is_valid():
      try:
        book_title = form.cleaned_data["search_input"]
        data= utils.fetch_books('title' ,str(book_title))
        context={"datas":data}
        return render(request,"books/book_list.html",context=context)
      except:
        return render(request, "books/book_list.html",context={"datas":None,"type":"Title","link":"title"})
    else:
      return render(request,"base.html",{"form":form,})



def author_search(request):
  if request.method == "GET":
    form=AuthorSearchForm()
    return render(request,"books/search.html", {"form":form,})
  
  if request.method == "POST":
    form=AuthorSearchForm(request.POST)
    if form.is_valid():
      try:
        book_author = form.cleaned_data["search_input"]
        data= utils.fetch_books("author",str(book_author))
        context={"datas":data}
        return render(request,"books/book_list.html",context=context)
      except:
        return render(request, "books/book_list.html",context={"datas":None,"type":"Author","link":"author"})
    else:
      return render(request,"base.html",{"form":form,})



def categories_search(request):
    if request.method == "GET":
      form=CategorySearchForm()
      return render(request,"books/search.html", {"form":form,})
  
    if request.method == "POST":
      form=CategorySearchForm(request.POST)
      if form.is_valid():
        try:
          book_category = form.cleaned_data["search_input"]
          data= utils.fetch_books('category',str(book_category))
          context={"datas":data}
          return render(request,"books/book_list.html",context=context)
        except:
          return render(request, "books/book_list.html",context={"datas":None,"type":"Categories", "link":"category"})
      else:
        return render(request,"base.html",{"form":form,})