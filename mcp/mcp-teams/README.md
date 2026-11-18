# mcp-teams

> MCP ficticio de prueba: no se conecta al sistema ni realiza operaciones reales.

## Qué hace

Servidor ficticio de lectura para canales y mensajes de Teams.

## Cuándo usarlo (y cuándo no)

Para probar consultas de lectura con datos de ejemplo; no envía mensajes.

## Cómo instalarlo en VS Code

Copia `config.example/vscode-mcp.json` a `.vscode/mcp.json` y ejecuta desde la carpeta de este MCP. Para levantar el servidor hace falta instalar el paquete MCP indicado por el proyecto consumidor.

## Ejemplo

Con un proyecto ficticio, las tools `listar_canales`, `leer_mensajes` devuelven un resultado de ejemplo.

## Configuración

`.env.example` contiene solo nombres de variables opcionales: TEAMS_EQUIPO, TEAMS_CANAL. No hacen falta para las respuestas ficticias y no deben añadirse secretos.

## Limitaciones

No consulta servicios reales; los resultados están escritos en el código de ejemplo.

## Responsable

equipo-demo
