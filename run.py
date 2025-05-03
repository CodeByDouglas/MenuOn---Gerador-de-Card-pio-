from app.init import create_app

app = create_app()

if __name__ == '__main__':
    # Por padrão roda em localhost:5000
    app.run(host='0.0.0.0', port=5000)
