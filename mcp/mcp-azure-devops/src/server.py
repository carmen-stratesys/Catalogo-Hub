"""Servidor MCP ficticio mcp-azure-devops; solo entrega datos de ejemplo."""
from mcp.server.fastmcp import FastMCP

from tools.leer_incidencias import leer_incidencias
from tools.leer_tareas import leer_tareas

servidor = FastMCP("mcp-azure-devops")
servidor.tool()(leer_incidencias)
servidor.tool()(leer_tareas)

if __name__ == "__main__":
    servidor.run()
