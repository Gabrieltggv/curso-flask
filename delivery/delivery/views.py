""" Extensão do Flask """


def init_app(app):
    """Inicialização de Extensões"""

    @app.route("/")
    def index():
        return "Hello Codeshow"

    @app.route("/contato"):
    def contato:
        return "<form><input type='Text'></input></form>"