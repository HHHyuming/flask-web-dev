from app import factory

app = factory.create_app()


if __name__ == '__main__':
    app.run(debug=True)