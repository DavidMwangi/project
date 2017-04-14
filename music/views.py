from django.http import HttpResponse

def index(request):

    response = """
        
        <html>
        
        <head><title>Music</title></head>
        
        <body>
        
        <h1>Welcome To The Music App Homepage</h1>
        
        </body>
        
        </html>
    
    """

    return (HttpResponse(response))

def detail(request):

    response = """
    
    
        <html>
        
        <head><title>Music</title></head>
        
        <body>
        
        <h1>Detail For Album id</h1> 
        
        </body>
        
        </html>
    
    """

    return HttpResponse(response)