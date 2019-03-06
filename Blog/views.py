from django.shortcuts import render,render_to_response

# Create your views here.
def home_blog(request):
    return render_to_response("blog.html")