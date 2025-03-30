#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP
from mcp.server.stdio import StdioServerTransport
from typing import Any, Dict

class ExampleServer:
    def __init__(self):
        self.server = FastMCP(
            {
                "name": "example-mcp-server",
                "version": "0.1.0"
            },
            {
                "capabilities": {
                    "tools": {},
                    "resources": {}
                }
            }
        )
        
        # Register tools
        @self.server.tool(
            name="example_tool",
            description="An example tool that echoes a message",
            input_schema={
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Message to echo"
                    }
                },
                "required": ["message"]
            }
        )
        async def example_tool(args: Dict[str, Any]) -> Dict[str, Any]:
            message = args["message"]
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Echo: {message}"
                    }
                ]
            }

    async def run(self):
        transport = StdioServerTransport()
        await self.server.connect(transport)
        print("MCP server running on stdio", file=sys.stderr)

if __name__ == "__main__":
    import asyncio
    import sys
    
    server = ExampleServer()
    asyncio.run(server.run())