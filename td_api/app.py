from application.create_app import create_app

app = create_app()

@app.route('/')
def hello():
    return "hey!"

if(__name__ == "__main__"):
    context = ('/https_certificates/server.crt', '/https_certificates/rootCA.key')
    app.run(ssl_context=context, host='0.0.0.0', port=8080)