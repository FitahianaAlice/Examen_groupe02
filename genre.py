import web
from navbar import Navbar
from database import Db
from footer import Footer

web.config.debug = True

urls = (
    '/accueil', 'index',
    '/artist', 'Artist',
    '/genre', 'Genre',
    '/employee', 'Employee',
    '/invoice', 'Invoice'
    '/genre', 'Genre'
)

class Genre:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        footer = Footer()
        footer_html = footer.get_footer()
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=8)
        grs=db.select('Genre', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-striped table-hover text-center w-75 m-auto rounded">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th>Genre</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for a in a2:
            result += '<tr>'
            for genre in grs:
                result += '<td>' +genre.Name+'</td>'
                break
        result += '</tbody>'
        result += '</table>'
        result += '</div>'
        result += footer_html
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
