"""Servidor MCP ficticio mcp-teams; solo entrega datos de ejemplo."""
from mcp.server.fastmcp import FastMCP

from tools.listar_canales import listar_canales
from tools.leer_mensajes import leer_mensajes

servidor = FastMCP("mcp-teams")
servidor.tool()(listar_canales)
servidor.tool()(leer_mensajes)

if __name__ == "__main__":
    servidor.run()
