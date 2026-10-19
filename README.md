# Thea — an open library your LLM can read

[Thea](https://thealibrary.org) is a free, people-curated knowledge graph that starts from places:
about **1.07 million places in Korea** from Korean public data, plus people, works, organizations, games
and dated records (new episodes, releases, openings) that people add and check.
It is read-only for AI, needs **no API key and no login**, and the data is **CC BY 4.0**.

> Sorry — for now, most of Thea is Korean. Other countries only have their regions set up so far. If you know places in your area, please add them at thealibrary.org.

Your model doesn't know what happened last week, or the noodle shop down the street.
The open web is mostly bot walls, logins and JavaScript. Thea is already open and already trimmed:
one entry is about 1 KB of fields, not a scraped page.

This repository is the **connection kit**: config snippets, tool definitions and a small example.

## Connect over MCP

One URL: `https://thealibrary.org/mcp` (Streamable HTTP, read-only, no auth).
Listed in the official MCP Registry as `org.thealibrary/thea`.

| Client | How |
|---|---|
| Claude (web, desktop) | Customize → Connectors → + Add → Add custom connector → the URL above. The free plan allows one custom connector. |
| ChatGPT (web) | chatgpt.com/plugins → + → Add custom MCP server → the URL above → No authentication → create as a plugin → install, then @ in a chat. Confirmed on Business, Enterprise, Edu; Plus and Pro not yet confirmed. |
| Gemini app | Not yet confirmed (open only to US, English, personal accounts; no-login servers unconfirmed) |
| Gemini CLI | `gemini mcp add --transport http thea https://thealibrary.org/mcp`, or `~/.gemini/settings.json`: `{"mcpServers": {"thea": {"httpUrl": "https://thealibrary.org/mcp"}}}` |
| LM Studio (0.3.17+) | Program → Install → Edit mcp.json: `{"mcpServers": {"thea": {"url": "https://thealibrary.org/mcp"}}}` |
| Ollama (ollmcp, third-party) | `ollmcp --mcp-server-url https://thealibrary.org/mcp --model <model>` |
| Open WebUI (0.6.31+, admin) | Admin Settings → Integrations → External Tool Servers → + → MCP (Streamable HTTP) → the URL above → auth None |
| Grok | grok.com/connectors → New Connector → Custom → the URL above |

An "unverified service" warning while connecting is normal for any connector you add yourself. Thea is read-only and takes no login or personal data.
Step-by-step guide in five languages: https://thealibrary.org/connect

Menu names change often; these were checked against each official doc on 2026-10-19.

## No MCP? Use function calling

`tools.json` (or the live copy at `https://thealibrary.org/ai/tools.json`) is in the OpenAI tool format
used by Ollama, llama.cpp, vLLM, SGLang and LM Studio. Give it to your model and run the tool it picks:

| Tool | Route | For |
|---|---|---|
| `thea_search` | `/ai/search?q=` | one entry whose name you know |
| `thea_find` | `/ai/find` | things matching conditions (e.g. noodle shops in a district, Japanese idols active in Korea, games released since a date) |
| `thea_entry` | `/ai/planet/{id}` | the full entry by id |

Plain text works too: `https://thealibrary.org/p/{id}.md`, and the overview at `https://thealibrary.org/llms.txt`.

`examples/ollama_tools.py` shows the whole loop with a local Ollama model.

## What you get back

Fields, links to related entries, and who wrote them: `written_by` is `human`, `ai`, `public_data` or `wiki`,
`checked_by` counts explorers who checked it against a source. AI-written fields nobody has checked yet are marked,
so your model can weigh them.

## License and attribution

This kit (code, config, examples): **MIT** — see `LICENSE`.
Data served by Thea: **CC BY 4.0**. Values that came from a source keep that source's terms (see each entry's `source`).
When you use it in an answer, add one line:

```
Source: [Thea](https://thealibrary.org) · CC BY 4.0
```

Missing something? Anyone can add it at [thealibrary.org](https://thealibrary.org), or post a request for it.
