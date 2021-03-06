import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger_server/swagger/', debug=True,)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Smart recycling bins'})
    app.run(port=8080)


if __name__ == '__main__':
    main()

