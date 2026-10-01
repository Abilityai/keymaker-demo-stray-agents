"""Score inbound leads 1-5 with an LLM call. Runs from cron, writes scored.csv. Nobody owns it."""
import csv, os, sys, json, urllib.request

PROMPT = "Score this inbound lead 1-5 for an automation agency. Reply with the number only.\n\n{lead}"

def score(lead):
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps({"model": "claude-sonnet-5", "max_tokens": 5,
                         "messages": [{"role": "user", "content": PROMPT.format(lead=lead)}]}).encode(),
        headers={"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01",
                 "content-type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)["content"][0]["text"].strip()

def main():
    rows = list(csv.DictReader(open("leads.csv")))
    with open("scored.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) + ["score"]); w.writeheader()
        for row in rows:
            row["score"] = score(json.dumps(row)); w.writerow(row)

if __name__ == "__main__":
    main()
