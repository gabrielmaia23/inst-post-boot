import os, sys, time, requests

IG_USER_ID = os.environ.get("IG_USER_ID", "17841441253956976")
TOKEN = os.environ["IG_TOKEN"]  # nunca escreva o token no código
BASE = "https://graph.facebook.com/v21.0"

image_url = sys.argv[1]
legenda = sys.argv[2] if len(sys.argv) > 2 else "legenda.txt"
caption = open(legenda, encoding="utf-8").read()

r = requests.post(f"{BASE}/{IG_USER_ID}/media", data={
    "image_url": image_url, "caption": caption, "access_token": TOKEN})
print("Container:", r.json())
r.raise_for_status()
creation_id = r.json()["id"]

for _ in range(20):
    s = requests.get(f"{BASE}/{creation_id}", params={
        "fields": "status_code", "access_token": TOKEN}).json()
    status = s.get("status_code")
    print("Status:", status)
    if status == "FINISHED":
        break
    if status == "ERROR":
        sys.exit("Erro ao processar a imagem. Confira se a URL é pública e JPEG.")
    time.sleep(3)

p = requests.post(f"{BASE}/{IG_USER_ID}/media_publish", data={
    "creation_id": creation_id, "access_token": TOKEN})
print("Publicado:", p.json())
p.raise_for_status()
