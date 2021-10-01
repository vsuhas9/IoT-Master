"""
OM2M view file
"""
from django.http import JsonResponse

# Create your views here


def om2m(request):
    """
    Main Function for calling OM2M
    :param request:
    :return:
    """
    print("Entered the function")
    return JsonResponse({"title": "success"}, safe=False, status=200)


def dummy(request):
    """
    Main Function for calling OM2M
    :param request:
    :return:
    """
    print("Hello")
    return JsonResponse({"title": "success"}, safe=False, status=200)
