from flask import Flask, jsonify

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi App DevOps · GCP</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: system-ui, sans-serif; background: #f8f9fa; color: #1c2833; }
    .topbar { display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem; background: white; border-bottom: 1px solid #e0e0e0; }
    .status { display: flex; align-items: center; gap: 8px; font-size: 13px; color: #3B6D11; font-weight: 500; }
    .dot { width: 9px; height: 9px; border-radius: 50%; background: #639922; }
    .region { font-size: 12px; color: #888; }
    .hero { text-align: center; padding: 3rem 1rem 2rem; }
    .hero h1 { font-size: 28px; font-weight: 600; margin-bottom: 10px; }
    .hero p { font-size: 16px; color: #555; margin-bottom: 1.5rem; }
    .url-bar { display: inline-flex; align-items: center; gap: 8px; background: #f1f1f1; border: 1px solid #ddd; border-radius: 8px; padding: 6px 14px; font-family: monospace; font-size: 13px; color: #555; }
    .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; max-width: 700px; margin: 2rem auto; padding: 0 1.5rem; }
    .stat { background: white; border: 1px solid #e0e0e0; border-radius: 10px; padding: 1rem; text-align: center; }
    .stat .num { font-size: 22px; font-weight: 600; color: #185FA5; }
    .stat .lbl { font-size: 12px; color: #888; margin-top: 4px; }
    .routes { max-width: 700px; margin: 0 auto 2rem; padding: 0 1.5rem; }
    .routes h2 { font-size: 16px; font-weight: 600; margin-bottom: 12px; color: #333; }
    .route { display: flex; align-items: center; gap: 12px; background: white; border: 1px solid #e0e0e0; border-radius: 10px; padding: 12px 16px; margin-bottom: 8px; }
    .method { font-size: 12px; font-weight: 600; padding: 3px 8px; border-radius: 6px; font-family: monospace; background: #E6F1FB; color: #0C447C; }
    .path { font-family: monospace; font-size: 14px; font-weight: 600; }
    .desc { font-size: 13px; color: #888; margin-left: auto; }
    .footer { text-align: center; padding: 1.5rem; font-size: 13px; color: #aaa; border-top: 1px solid #e0e0e0; margin-top: 1rem; background: white; }
  </style>
</head>
<body>
  <div class="topbar">
    <div class="status"><div class="dot"></div>online</div>
    <span class="region">Cloud Run · us-central1</span>
  </div>
  <div class="hero">
    <h1>Mi App DevOps en GCP</h1>
    <p>Pipeline CI/CD con Cloud Build, Artifact Registry y Cloud Run.</p>
    <div class="url-bar">&#128274; mi-app-devops-apbg33n2ya-uc.a.run.app</div>
  </div>
  <div class="stats">
    <div class="stat"><div class="num">100%</div><div class="lbl">uptime</div></div>
    <div class="stat"><div class="num">&lt;3 min</div><div class="lbl">commit a prod</div></div>
    <div class="stat"><div class="num">2</div><div class="lbl">rutas activas</div></div>
    <div class="stat"><div class="num">auto</div><div class="lbl">escalado</div></div>
  </div>
  <div class="routes">
    <h2>Rutas disponibles</h2>
    <div class="route"><span class="method">GET</span><span class="path">/</span><span class="desc">Esta página</span></div>
    <div class="route"><span class="method">GET</span><span class="path">/health</span><span class="desc">Health check JSON</span></div>
  </div>
  <div class="footer">Desplegado con DevOps · Cloud Build + Cloud Run · GCP</div>
</body>
</html>"""

@app.route("/")
def home():
    return HTML

@app.route("/health")
def health():
    return jsonify({"healthy": True, "status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)