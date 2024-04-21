from django.shortcuts import render

# Create your views here.
def getPostList(request):
    return render(request, 'blog/post_list.html', {})
