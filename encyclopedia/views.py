from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage

from . import util

import markdown2 
import random 

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    return render(request , "encyclopedia/new_page.html"  )

def edit_page(request , title):
    return render(request , "encyclopedia/edit_page.html" , {
        "data" : util.get_entry(title) , "title" : title
    } )

def title_page(request ,title):

    if title == 'random' :
        title = random.choice(util.list_entries())

    if request.method == "POST" :
        if 'content' not in request.POST :
            title = request.POST['q']
            if title not in util.list_entries() :
                search_list = []
                for entry in util.list_entries() :
                    if entry.find(title) != -1 :
                        search_list.append(entry)
        
                return render(request , "encyclopedia/search.html" ,{
                    "entries": search_list   
                } )
        else :
            if 'title' not in request.POST :
                util.save_entry(title , request.POST['content'])

            else :
                filename = f"entries/{request.POST['title']}.md"
                if default_storage.exists(filename):
                    return render(request , "encyclopedia/new_page.html"  )
                else :
                    util.save_entry(request.POST['title'] , request.POST['content'])
                    title = request.POST['title'] 

    if util.get_entry(title) == None :
        return render(request , "encyclopedia/title_page.html" , {
            "data": None , "title":title
        } )
    else :
        return render(request , "encyclopedia/title_page.html" , {
            "data": markdown2.markdown(util.get_entry(title)) , "title":title
        } )
