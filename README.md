# Catalogo-Hub

Catálogo de componentes de IA (skills, MCP y agentes) que consulta el **AI Agent Hub**, la prueba de concepto de Nexus Academy 2026. Todo lo que hay aquí es **ficticio**: sirve para probar el recorrido, no para usar con datos reales.

## Estructura

| Carpeta | Qué contiene |
|---|---|
| `skills/` | Una carpeta por skill: `SKILL.md`, `hub.yaml` y `CAMBIOS.md` |
| `mcp/` | Un MCP por sistema, con `README.md`, `hub.yaml`, `src/`, `tests/` y `config.example/` |
| `agentes/` | Un agente por objetivo, con `instrucciones.md`, `agente.yaml`, `evaluacion/` y `tests/` |
| `estandar/` | Plantillas de ficha (`hub.yaml`) y `politicas.md`. **No son componentes** |

Cada componente lleva su ficha `hub.yaml` con la descripción, cuándo usarlo, las capacidades, el efecto (`lectura`, `escritura` o `impacto`) y la versión. No lleva secretos: solo un `.env.example` con nombres de variables.

## Ramas

- **`principal`**: lo aprobado y ya probado. Es lo que ve todo el equipo.
- **`pruebas`**: componentes aprobados que aún están en prueba. Solo los técnicos los ven. Siempre contiene todo lo de `principal`.

## Cómo entra un componente

1. Se aporta desde el Hub: se anonimiza y lo revisan los agentes Documentador, Comparador y Seguridad.
2. El Hub abre una PR hacia `pruebas` y publica el estado `aihub/agentes`.
3. **Otra persona distinta del autor** la aprueba y la fusiona.
4. Más adelante, una PR de `pruebas` a `principal` lo promueve.

Ambas ramas están protegidas: exigen PR con una aprobación de otra persona, y `pruebas` exige además el estado `aihub/agentes`.
