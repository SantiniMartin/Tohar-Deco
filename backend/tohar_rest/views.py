from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Tohar-Deco API está operativa. Visita /admin/ o /api/auth/ para endpoints."})
