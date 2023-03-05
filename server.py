import web
from accueil import index

web.config.debug = False

urls = (
    '/','accueil',
    '/accueil', 'index'
)

class accueil:
    def GET(self):
        return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
     <title>Animation background</title>
     <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
      crossorigin="anonymous"
    />
   
    
  <style>
    * {
      margin: 0;
      padding: 0;
      font-family: "Candara";
      overflow-x: hidden;
    }

    section {
      position: relative;
      width: 100%;
      background: url(https://images.alphacoders.com/808/thumbbig-80833.webp) center;
      }

    section h2 {
      font-family: Cambria, Cochin, Georgia, Times, "Times New Roman", serif;
      position: relative;
      width: 100%;
      height: 100%;
      margin-top: -240px;
      margin-left: 300px;
      text-align: center;
      line-height: 100vh;
      font-size: 5vw;
      color: #fff;
      font-weight: 700;
    }

    .banner {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      display: flex;
      flex-wrap: wrap;
    }

    .banner .blocks {
      position: relative;
      display: block;
      width: 10vw;
      height: 10vw;
      animation: animate 2s ease-in-out forwards;
    }

    .banner .blocks:nth-child(even) {
      animation: animate 4s ease-in-out forwards;
    }

    .banner .blocks:nth-child(7n + 3) {
      animation: animate 9.5s ease-in-out forwards;
    }

    .banner .blocks:nth-child(7n + 7) {
      animation: animate 5.5s ease-in-out forwards;
    }

    @keyframes animate {
      0% {
        opacity: 0;
        transform: scale(0) translateY(900px);
      }
      50% {
        opacity: 1;
        background: url("https://i.pinimg.com/originals/fe/1b/8e/fe1b8e5e62ee2cef454f11432e4b24e8.jpg");
      }
      100% {
        opacity: 1;
        transform: scale(1) translateY(0px);
      }
    }
  </style>
  </head>
  <body id="accueil">
    <div class="container">
      <header
        class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom"
      >
        <a
          href="/"
          class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none"
        >
          <svg class="bi me-2" width="40" height="32">
            <use xlink:href="#bootstrap" />
          </svg>
          <img src="https://st4.depositphotos.com/11953928/24769/v/450/depositphotos_247699532-stock-illustration-music-icon-cartoon.jpg" width="120px" class="text-dark rounded" alt="Logo">
        </a>

        <ul class="nav nav-pills mt-4">
          <li class="nav-item">
            <a href="#accueil" class="nav-link fs-4" aria-current="page">Accueil</a>
          </li>
          <li class="nav-item">
            <a href="#membre" class="nav-link fs-4">Membres du groupe</a>
          </li>
          <li class="nav-item"><a href="/accueil" class="nav-link fs-4">Voir tout >>></a></li>
        </ul>
      </header>
    </div>

    <section>
      <h2>THE MUSIC WEBSITE</h2>
      <div class="banner">
        <div class="blocks"></div>
      </div>
    </section>
    <article id="membre" class="text-center mt-5">
      <h1>Les membres du Groupe 02</h1>
      <div class="row mt-5 border p-4 rounded bg-primary">
        <div class="col-md-6">
          <img src="https://cdn-icons-png.flaticon.com/512/5556/5556487.png" alt="avatar" class="rounded" width="25%" />
        </div>
        <div class="col-md-6 mt-5">
          <h2 class="border-bottom w-75 m-auto text-light">Njiva Ariaina</h2>
          <span class="fs-4">DTS Web: L1</span>
        </div>
      </div>
      <div class="row mt-5 mb-5 border p-4 rounded bg-success">
        <div class="col-md-6 mt-5">
          <h2 class="border-bottom text-light w-75 m-auto">Fitahiana Valisoa</h2>
          <span class="fs-4">License: L1</span>
        </div>
        <div class="col-md-6">
          <img src="https://previews.123rf.com/images/juliasart/juliasart1704/juliasart170400208/75545532-vecteur-ic%C3%B4ne-fille-avatar-femme-ic%C3%B4ne-de-visage-style-de-bande-dessin%C3%A9e.jpg" alt="avatar" class="rounded" width="25%" />
        </div>
      </div>
    </article>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-Kfw/ZfLsBbsW/v98ZDd2Q89fUJi6UwH6mE2unQ2XgU+cOaMrmZxBKjPLdLgmhC5/" crossorigin="anonymous"></script>

 <script>
      const banner = document.getElementsByClassName("banner")[0];
      const blocks = document.getElementsByClassName("blocks");

      for (var i = 1; i < 400; i++) {
        banner.innerHTML += "<div class='blocks'></div>";
        blocks[i].style.animationDelay = `${i * 0.05}s`;
      }
    </script>
  </body>
</html>
'''
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
