import web
from navbar import Navbar
from database import Db
from footer import Footer

web.config.debug = True

urls = (
    '/accueil', 'index',
    '/artist', 'Artist',
)

class Artist:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        footer = Footer()
        footer_html = footer.get_footer()
        d = Db()
        db = d.getDb()
        artists = db.select('Artist', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-border w-75 m-auto">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th class="text-center">#</th>'
        result += '<th class="text-center">Artist Name</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for artist in artists:
            albums = db.select('Album', where='ArtistId=$id', vars={'id': artist.ArtistId})
            result += '<tr>'
            result += '<td class="bg-dark text-white text-center">' + str(artist.ArtistId) + '</td>'
            result += '<td class="text-center">' + artist.Name + '</td>'
            result += '</tr>'
        result += '</tbody>'
        result += '</table>'
        result += '</div>'
        result += footer_html
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
