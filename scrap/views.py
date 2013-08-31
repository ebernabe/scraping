# Create your views here.
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render_to_response
from scrap.models import *	
from django.conf import settings
import urllib3
from lxml.cssselect import CSSSelector         
import lxml.html
import extraction
import string
import re
import cgi
import unicodedata


def scrapping(request):
	while 1:
		all_users = []
		u_t = ""
		url = ""
		chatml =  "https://chat.mejorando.la/"
		http2 = urllib3.PoolManager()
		r2 = http2.request('GET', chatml)
		chatmlhtml = r2.data
		root = lxml.html.fromstring(chatmlhtml)
		for el in root.cssselect('a.user'):
			all_users.append(lxml.html.tostring(el))
			u_t = el.text_content().strip()
			elements = el.cssselect("a.user")
			for element in elements:
				url = element.get('href')
			try:
				p = Chat.objects.get(usuario_twitter=u_t)
				pass
			except Chat.DoesNotExist:
				p = Chat(usuario_twitter=u_t, url_twitter=url)
				p.save()
				pass
	return render_to_response('a.html', {"chatmlhtml": chatmlhtml,"all_users":all_users})


