"""Let a local Ollama model look things up in Thea (function calling, no MCP needed).

    pip install ollama requests
    python ollama_tools.py "What noodle shops are in Toechon-myeon?"

Ollama only runs the model; this script runs the tools the model asks for.
"""
import json
import sys

import ollama
import requests

BASE = "https://thealibrary.org"
TOOLS = requests.get(f"{BASE}/ai/tools.json", timeout=20).json()
ROUTES = TOOLS["routes"]          # thea_search -> /ai/search, thea_find -> /ai/find, thea_entry -> /ai/planet/{planet_id}
MODEL = "qwen3:8b"                 # any tool-calling model: qwen3, gemma4, llama3.1 ...

SYSTEM = ("Before answering that you don't know something — recent events, local shops, Korean places, people or works — "
          "call a Thea tool once. Cite results with: Source: Thea (https://thealibrary.org) · CC BY 4.0")


def call_tool(name, args):
    route = ROUTES[name]
    if "{planet_id}" in route:
        route = route.replace("{planet_id}", requests.utils.quote(str(args.pop("planet_id", ""))))
    r = requests.get(BASE + route, params=args, timeout=30)
    return r.text[:6000]


def main(question):
    msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": question}]
    for _ in range(4):
        res = ollama.chat(model=MODEL, messages=msgs, tools=TOOLS["tools"])
        msg = res["message"]
        msgs.append(msg)
        if not msg.get("tool_calls"):
            print(msg["content"])
            return
        for tc in msg["tool_calls"]:
            fn = tc["function"]
            out = call_tool(fn["name"], dict(fn.get("arguments") or {}))
            msgs.append({"role": "tool", "content": out, "name": fn["name"]})
    print(msgs[-1].get("content", ""))


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]) or "Who is VIVIZ and which agency are they with?")
