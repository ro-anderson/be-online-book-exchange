from src.main.configs import app
from os import environ

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=environ.get('PORT', 5001))
