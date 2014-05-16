from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from django.http import HttpResponse
from BookmarkManager.dbUtils import *
@csrf_exempt
def fn(request):
	data = request.POST['data']
	index = data.find(",")
	if index == -1:
		RESPONSE_CODE , BOOKMARK_URL = search(data)
	else:
		RESPONSE_CODE , BOOKMARK_URL = insert(data,index)
	return HttpResponse(RESPONSE_CODE + " " + BOOKMARK_URL)