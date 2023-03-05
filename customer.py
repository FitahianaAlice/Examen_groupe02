import web
from navbar import Navbar
from database import Db
from footer import Footer

web.config.debug = True

urls = (
    '/', 'index',
    '/artist', 'Artist',
    '/genre', 'Genre',
    '/employee', 'Employee',
    '/invoice', 'Invoice',
    '/invoiceLine', 'InvoiceLine',
    '/customer', 'Customer'
)

class Customer:
    def GET(self):
        navbar = Navbar()
        navbar_html = navbar.get_navbar()
        d = Db()
        db = d.getDb()
        a2=db.select('Album', limit=8)
        cstm=db.select('Customer', limit=8)
        result = navbar_html
        result += '<div class="container">'
        result += '<table class="table table-striped text-center w-75 m-auto">'
        result += '<thead class="bg-primary text-white">'
        result += '<tr>'
        result += '<th>Customer</th>'
        result += '</tr>'
        result += '</thead>'
        result += '<tbody>'
        for a in a2:
            result += '<tr>'
            for customer in cstm:
                result += '<td>' +customer.FirstName+'</td>' 
                break
        result += '</tr>'
        result += '</table>'
        result += '</div>'
        result += '</body></html>'
        result += footer_html
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
