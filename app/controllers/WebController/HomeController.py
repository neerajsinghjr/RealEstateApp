from ..Controller import *          # Base Controller

class HomeController(Controller):

    def __init__(self):
        pass

    def index(self, request):
        return render(request, "web/views/index.html")


    def about(self, request):
        return render(request, "web/views/about.html")


    def contact(self, request):
        return render(request, "web/views/contact.html")


    def search(self, request):
        return render(request, "web/views/index.html")


    def dashboard(self, request):
        return render(request, 'web/views/dashboard.html')


    def listings(self, request):
        return render(request, 'web/views/listings.html')
    

    def listing(self, request, eid):
        return render(request, 'web/views/listing.html')
