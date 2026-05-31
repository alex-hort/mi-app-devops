from flask import Flask, jsonify

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi App DevOps · GCP</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: system-ui, sans-serif;
      background: #fff5f5;
      color: #2d0000;
    }

    .topbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 2rem;
      background: white;
      border-bottom: 2px solid #ef9a9a;
    }

    .status {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      color: #b71c1c;
      font-weight: 600;
    }

    .dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: #d32f2f;
      box-shadow: 0 0 8px rgba(211, 47, 47, 0.5);
    }

    .region {
      font-size: 12px;
      color: #888;
    }

    .hero {
      text-align: center;
      padding: 3rem 1rem 2rem;
    }

    .hero h1 {
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 10px;
      color: #b71c1c;
    }

    .hero p {
      font-size: 16px;
      color: #555;
      margin-bottom: 1.5rem;
    }

    .url-bar {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #ffebee;
      border: 1px solid #ef9a9a;
      border-radius: 8px;
      padding: 8px 16px;
      font-family: monospace;
      font-size: 13px;
      color: #b71c1c;
      font-weight: 600;
    }

    .stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 12px;
      max-width: 700px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }

    .stat {
      background: white;
      border: 1px solid #ef9a9a;
      border-radius: 10px;
      padding: 1rem;
      text-align: center;
      transition: transform 0.2s;
    }

    .stat:hover {
      transform: translateY(-2px);
    }

    .stat .num {
      font-size: 22px;
      font-weight: 700;
      color: #c62828;
    }

    .stat .lbl {
      font-size: 12px;
      color: #888;
      margin-top: 4px;
    }

    .routes {
      max-width: 700px;
      margin: 0 auto 2rem;
      padding: 0 1.5rem;
    }

    .routes h2 {
      font-size: 18px;
      font-weight: 700;
      margin-bottom: 12px;
      color: #b71c1c;
    }

    .route {
      display: flex;
      align-items: center;
      gap: 12px;
      background: white;
      border: 1px solid #ef9a9a;
      border-radius: 10px;
      padding: 12px 16px;
      margin-bottom: 8px;
    }

    .method {
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      font-family: monospace;
      background: #ffebee;
      color: #b71c1c;
    }

    .path {
      font-family: monospace;
      font-size: 14px;
      font-weight: 700;
    }

    .desc {
      font-size: 13px;
      color: #888;
      margin-left: auto;
    }

    .footer {
      text-align: center;
      padding: 1.5rem;
      font-size: 13px;
      color: #b71c1c;
      border-top: 1px solid #ef9a9a;
      margin-top: 1rem;
      background: white;
    }
  </style>
</head>
<body>
  <div class="topbar">
    <div class="status">
      <div class="dot"></div>
      ONLINE
    </div>
    <span class="region">Cloud Run · us-central1</span>
  </div>

  <div class="hero">
    <h1>🚀 Mi App DevOps en GCP</h1>
    <p>Pipeline CI/CD con Cloud Build, Artifact Registry y Cloud Run.</p>

    <div class="url-bar">
      🔒 mi-app-devops-apbg33n2ya-uc.a.run.app
    </div>
  </div>

  <div class="stats">
    <div class="stat">
      <div class="num">100%</div>
      <div class="lbl">UPTIME</div>
    </div>

    <div class="stat">
      <div class="num">&lt;3 min</div>
      <div class="lbl">COMMIT A PROD</div>
    </div>

    <div class="stat">
      <div class="num">2</div>
      <div class="lbl">RUTAS ACTIVAS</div>
    </div>

    <div class="stat">
      <div class="num">AUTO</div>
      <div class="lbl">ESCALADO</div>
    </div>
  </div>

  <div class="routes">
    <h2>Rutas disponibles</h2>

    <div class="route">
      <span class="method">GET</span>
      <span class="path">/</span>
      <span class="desc">Esta página</span>
    </div>

    <div class="route">
      <span class="method">GET</span>
      <span class="path">/health</span>
      <span class="desc">Health check JSON</span>
    </div>
  </div>

  <div class="footer">
    Desplegado con DevOps · Cloud Build + Cloud Run · GCP
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML

@app.route("/health")
def health():
    return jsonify({
        "healthy": True,
        "status": "ok"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)