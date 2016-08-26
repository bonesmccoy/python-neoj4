import connexion

app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('api-definition.yml')
app.run(port=8020, debug=True)