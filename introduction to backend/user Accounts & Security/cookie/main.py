import webapp2
import jinja2
import os 
from hashed  import *
#################################

from google.appengine.ext import db
template_dir = os.path.join(os.path.dirname(__file__),'templates')

jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)


class Handler(webapp2.RequestHandler):
	v=0
	"""docstring for Hanfler"""
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)
	def render_str(self,template,**params):
		t=jinja_env.get_template(template)
		return t.render(params)

	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))

class MainPage(Handler):
    def get(self):
    	
    	visits =0 

    	visit_cookie_str = self.request.cookies.get('visits')
    	if visit_cookie_str:
    		cookie_val=check_secure_val(visit_cookie_str)
    		if(cookie_val):
    			visits=int(cookie_val)
    	#check if visits is integer
    	"""
    	if visits.isdigit():
    		visits = int(visits)+1
    	else : visits=0
    	"""
    	visits+=1
    	new_cookie_val=make_secure_val(str(visits))
    	self.response.headers.add_header('Set-Cookie','visits=%s'%new_cookie_val)
    
    	if ( visits > 10):self.write("you are the best")
    	else:	self.write("you've been here %s"%visits)
    	############
    	self.write("<br> views {0}".format (Handler.v))
    	Handler.v+=1
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
