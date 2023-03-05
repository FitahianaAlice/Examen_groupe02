import web
from navbar import Navbar
from database import Db
from footer import Footer

web.config.debug = True

urls = (
    '/', 'index',
    '/album', 'Album',
    '/artist', 'Artist',
    '/employee', 'Employee',
    '/invoice', 'Invoice'
)

class Employee:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        footer = Footer()
        footer_html = footer.get_navbar()
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=8)
        employe=db.select('Employee', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-border table-striped table-hover w-75 m-auto"">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th class="text-center" >Employee</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for a in a2:
            result += '<tr>'
            for employee in employe:
                result += '<td class="text-center" >' +employee.LastName+'</td>'
                break
        result += '</tbody>'
        result += '</table>'
        result += '</div>'
        result += footer_html
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
