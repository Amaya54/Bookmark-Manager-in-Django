from models import *
from django.db import IntegrityError, DatabaseError
from django.core.exceptions import ValidationError

def search(data):
	data = ","+data+","
	try:
		user = bookmark.objects.get(tag__icontains = data)
		BOOKMARK_URL = user.url
	except ValidationError, e:
		BOOKMARK_URL = "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_VALIDATION_ERROR"
	except IntegrityError, e:
		BOOKMARK_URL = "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_INTEGRITY_ERROR"		
	except DatabaseError, e:
		BOOKMARK_URL = "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_DATABASE_ERROR"
	except Exception, e:
		BOOKMARK_URL = "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_GENERIC_ERROR"
	else :
		RESPONSE_CODE = "RESPONSE_CODE_SUCCESS"
	return RESPONSE_CODE,BOOKMARK_URL

def insert(data,index):
	url = data[:index]
	tag = data[index:] + ','
	try:
		user = bookmark(url = url,tag = tag)
		user.save()
	except ValidationError, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_VALIDATION_ERROR"
	except IntegrityError, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_INTEGRITY_ERROR"		
	except DatabaseError, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_DATABASE_ERROR"
	except Exception, e:
		print "Exception "+str(e)
		RESPONSE_CODE = "RESPONSE_CODE_GENERIC_ERROR"
	else :
		RESPONSE_CODE = "RESPONSE_CODE_SUCCESS"
	return RESPONSE_CODE , "BOOKMARK SAVED"