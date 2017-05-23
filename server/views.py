from django.http import JsonResponse

def home(request):
    return JsonResponse('good bye world', safe=False)
