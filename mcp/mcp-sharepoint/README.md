# mcp-sharepoint

> MCP ficticio de prueba: no se conecta al sistema ni realiza operaciones reales.

## Qué hace

Servidor ficticio de lectura para documentos y metadatos.

## Cuándo usarlo (y cuándo no)

Para probar búsquedas con resultados de ejemplo; no se conecta a SharePoint.

## Cómo instalarlo en VS Code

Copia `config.example/vscode-mcp.json` a `.vscode/mcp.json` y ejecuta desde la carpeta de este MCP. Para levantar el servidor hace falta instalar el paquete MCP indicado por el proyecto consumidor.

## Ejemplo

Con un proyecto ficticio, las tools `buscar_documentos`, `leer_metadatos` devuelven un resultado de ejemplo.

## Configuración

`.env.example` contiene solo nombres de variables opcionales: SHAREPOINT_SITIO, SHAREPOINT_BIBLIOTECA. No hacen falta para las respuestas ficticias y no deben añadirse secretos.

## Limitaciones

No consulta servicios reales; los resultados están escritos en el código de ejemplo.

## Responsable

equipo-demo
