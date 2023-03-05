import web

class Navbar:
    def get_navbar(self):
        result = '<html><head><title>Test Groupe 02</title>'
        result += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">'
        result += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css"/>'
        result += '</head>'
        result += '<a href="/" data-toggle="tooltip" title="Accueil" class="btn btn-info"><i class="fa fa-home m-2"></i></a>'
        result += '<nav class="navbar navbar-expand navbar-light bg-info w-75 mt-4 mb-4 ml-auto mr-auto rounded" >'
        result += '<div class="container justify-content-md-center">'
        result += '<ul class="navbar-nav">'
        result += '<li class="nav-item"><a class="nav-link text-light" aria-current="page" href="/accueil">All</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" aria-current="page" href="/album">Album</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/artist">Artist</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/customer">Customer</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/genre">Genre</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/employee">Employee</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/invoice">Invoice</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/invoiceLine">InvoiceLine</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/mediaType">MediaType</a></li>'
        result += '<li class="nav-item"><a class="nav-link text-light" href="/playlist">Playlist</a></li>'
        result += '</ul>'
        result += '</div>'
        result += '</nav>'
        return result
