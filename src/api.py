from src.monitoring import PRED_DIST
@app.get('/metrics')
def metrics(): return PRED_DIST