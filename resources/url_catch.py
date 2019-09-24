from flask_restful import Resource
from models.url import UrlModel
from flask import redirect

class SendUrl( Resource ):
    def get(self, url):    
        url_find = UrlModel.get_by_shorted( url )
        if url_find is None: 
            return redirect("/", code=302)
        return redirect(url_find.get_real_url(), code=302)