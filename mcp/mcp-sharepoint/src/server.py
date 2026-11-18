"""Servidor MCP ficticio mcp-sharepoint; solo entrega datos de ejemplo."""
from mcp.server.fastmcp import FastMCP

from tools.buscar_documentos import buscar_documentos
from tools.leer_metadatos import leer_metadatos

servidor = FastMCP("mcp-sharepoint")
servidor.tool()(buscar_documentos)
servidor.tool()(leer_metadatos)

if __name__ == "__main__":
    servidor.run()
