from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {"x": "hehe",
               "y": "bwuh",
               "z": ["I", "am", "a", "list", "!"],
               }
    print("Signed in as " + str(request.user))
    return render(request, "home.html", context)
