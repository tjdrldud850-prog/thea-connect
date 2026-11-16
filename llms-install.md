# Installing Thea (for AI agents such as Cline)

Thea is a **remote** MCP server. There is nothing to install, build or run locally, and there is **no API key and no login**.

- URL: `https://thealibrary.org/mcp`
- Transport: Streamable HTTP
- Auth: none
- Access: read-only

## Cline

Add this entry under `mcpServers` in `cline_mcp_settings.json`. If the file does not exist yet, create it with exactly this content.

- Cline CLI: `~/.cline/data/settings/cline_mcp_settings.json` (or the path in `CLINE_MCP_SETTINGS_PATH`)
- Cline in VS Code: MCP Servers icon → Configure → Configure MCP Servers opens the file. Or use the Remote Servers tab: name `thea`, URL `https://thealibrary.org/mcp`, transport Streamable HTTP.


```json
{
  "mcpServers": {
    "thea": {
      "type": "streamableHttp",
      "url": "https://thealibrary.org/mcp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

Keep `"type": "streamableHttp"`: without it Cline falls back to the legacy SSE transport, which Thea does not serve.

## Check that it works

The server exposes read-only tools. The main three:

- `thea_search`: one entry by name, e.g. `{"q": "Gyeongbokgung"}`
- `thea_find`: entries matching conditions (place, kind, date)
- `thea_entry`: the full entry by id (`planet_id`)

(`search` and `fetch` are the same data in the shape ChatGPT expects.)

Call `thea_search` with any well-known Korean place name. A result with an `id` means the connection works.

## Other clients

See the table in README.md.
