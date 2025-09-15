
from flask import Flask, jsonify, render_template
from scraper import get_all_prices
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
cache = {"data": {}, "last_updated": None}

def update_prices():
    global cache
    cache["data"] = get_all_prices()

# Actualizar precios al iniciar
update_prices()

# Programar actualizaciones cada 5 minutos
scheduler = BackgroundScheduler()
scheduler.add_job(update_prices, 'interval', minutes=5)
scheduler.start()

# Ruta para servir el HTML
@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/api/precios")
def precios():
    return jsonify(cache["data"])

if __name__ == "__main__":
    app.run(debug=True)
