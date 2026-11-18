"""Servidor MCP ficticio mcp-jira; solo entrega datos de ejemplo."""
from mcp.server.fastmcp import FastMCP

from tools.leer_tickets import leer_tickets
from tools.leer_sprints import leer_sprints

servidor = FastMCP("mcp-jira")
servidor.tool()(leer_tickets)
servidor.tool()(leer_sprints)

if __name__ == "__main__":
    servidor.run()
