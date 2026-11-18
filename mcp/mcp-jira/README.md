# mcp-jira

> MCP ficticio de prueba: no se conecta al sistema ni realiza operaciones reales.

## Qué hace

Servidor ficticio de lectura para tickets y sprints de Jira.

## Cuándo usarlo (y cuándo no)

Para probar consultas de lectura con datos de ejemplo; no crea ni modifica elementos.

## Cómo instalarlo en VS Code

Copia `config.example/vscode-mcp.json` a `.vscode/mcp.json` y ejecuta desde la carpeta de este MCP. Para levantar el servidor hace falta instalar el paquete MCP indicado por el proyecto consumidor.

## Ejemplo

Con un proyecto ficticio, las tools `leer_tickets`, `leer_sprints` devuelven un resultado de ejemplo.

## Configuración

`.env.example` contiene solo nombres de variables opcionales: JIRA_URL, JIRA_PROYECTO. No hacen falta para las respuestas ficticias y no deben añadirse secretos.

## Limitaciones

No consulta servicios reales; los resultados están escritos en el código de ejemplo.

## Responsable

equipo-demo
