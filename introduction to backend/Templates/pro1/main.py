import webapp2
html="""
<form>
	<h2>Add a Food </h2>
	<input type="text" name="food">
	%s
	<button>add</button>

</form>
"""
item_html="<li>%s</li>"
hidden_html= """
	<input type="hidden" name="food" value="%s">
"""
shopping_list_html="""
<br>
<br>
<h2>Shopping List</h2>
%s 
</ul>
"""
class Handler(webapp2.RequestHandler):
	"""docstring for Hanfler"""
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)
		
class MainPage(Handler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        output = html
        out_hidden=""
        #ser.write(out_hidden)
        items = self.request.get_all("food")
        if items:
	        	output_items=""
	       		for item in items:
	        	    out_hidden+=hidden_html%item
	        	    output_items+=item_html%item

	       		output_shopping = shopping_list_html%output_items
	      		output +=output_shopping
	  	#output = output%"out_hidden"
        self.write(output%out_hidden)
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
