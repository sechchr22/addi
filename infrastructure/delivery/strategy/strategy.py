""" Strategy to service running."""
# Esta va a ser la estrategía de arranque de la app
# TODO: falta hacerle un START()

import uvicorn
from infrastructure.delivery.api import app

# Strategy for local environment
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
