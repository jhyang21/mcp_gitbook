# MCP Server Example

A simple MCP (Model Context Protocol) server implementation using the Python MCP SDK with FastMCP.

## Setup

1. Install dependencies using uv:
```bash
uv add "mcp[cli]" requests python-dotenv
```

## Running the Server

Run the server:
```bash
python src/mcp_gitbook/main.py
```

## Available Tools

### example_tool
An example tool that echoes a message back.

Input schema:
```json
{
    "type": "object",
    "properties": {
        "message": {
            "type": "string",
            "description": "Message to echo"
        }
    },
    "required": ["message"]
}
```

Example usage:
```json
{
    "method": "call_tool",
    "params": {
        "name": "example_tool",
        "arguments": {
            "message": "Hello, MCP!"
        }
    }
}
