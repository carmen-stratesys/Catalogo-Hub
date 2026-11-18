"""Servidor MCP ficticio mcp-github; solo entrega datos de ejemplo."""
from mcp.server.fastmcp import FastMCP

from tools.leer_repositorios import leer_repositorios
from tools.leer_issues import leer_issues

servidor = FastMCP("mcp-github")
servidor.tool()(leer_repositorios)
servidor.tool()(leer_issues)

if __name__ == "__main__":
    servidor.run()
