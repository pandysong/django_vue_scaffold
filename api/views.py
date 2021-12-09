from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware import csrf

# Create your views here.


@require_http_methods(["POST", "OPTIONS"])
def handle_upload(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    if request.method == "POST":
        if 'file' in request.FILES:
            response = JsonResponse({'filesize': request.FILES['file'].size})
        else:
            response = JsonResponse({'error': 'missing files'})
    else:
        response = JsonResponse({'options': ''})
    return response


@ensure_csrf_cookie
def get_csrf(request):
    ''' return csrf cookie
        to the client so that client could POST to server
        using the token
    '''
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = csrf.get_token(request)
    return response
