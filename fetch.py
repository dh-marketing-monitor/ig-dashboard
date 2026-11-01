import json, os, urllib.request, urllib.parse

TOKEN = os.environ["IG_TOKEN"]
USER_ID = os.environ["IG_USER_ID"]
ACCOUNTS = ["dubaiholding", "mubadala", "nakheelofficial", "emaardubai", "adq_official", "publicinvestmentfund"]  # add more handles here
FIELDS = ("business_discovery.username({h}){{username,name,profile_picture_url,"
          "followers_count,media_count,media.limit(24){{caption,media_type,media_url,"
          "thumbnail_url,permalink,timestamp,like_count,comments_count}}}}")

out = []
for h in ACCOUNTS:
    q = urllib.parse.urlencode({"fields": FIELDS.format(h=h), "access_token": TOKEN})
    url = f"https://graph.facebook.com/v21.0/{USER_ID}?{q}"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            out.append(json.load(r)["business_discovery"])
    except Exception as e:
        out.append({"username": h, "error": str(e)})

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False)
print("Saved", len(out), "accounts")
