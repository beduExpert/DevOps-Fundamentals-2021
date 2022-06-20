POSTWORK
Sesión 08
Manejo de alertas con Alertmanager

🎯 Objetivos

Configurar un Alertmanager.
Conectar el Alertmanager con Prometheus.
Conectar el Alertmanager con Jenkins.


🚀 Desarrollo

Prometheus tiene la habilidad de levantar alarmas cuando una condicion se cumple, pero no es un manejador e alertas, para esto existe otro programa hermano que desduplica alertas y las agrupa para su manejo por un operador, para enviar notificaciones de la alerta o para ejecutar un weghook de jenkins.

Como nuestro project de jenkins reconstruye el conenedor, podemos emplear Alertmanager para que al momento de recibir al alerta de que un microservico esta caído ejecutar el projecto Jenkins y levantar el contenedor nuevamente.

Los pasos a seguir:
- Preparar el contenedor para Alertmanager.
- Configurar Prometheus para que envie alertas al Alertmanager.
- Configurar Alertmanager con las rutas de cada microservicio.
- Agregar plugin `Generic Webhook` en Jenkins. [Imágen](./webhook-plugin.png)
- Configurar projectos de Jenkins para activar la contrucción via Webhook. [Imágen](./project-configs.png)

💡 Consulta [en esta carpeta](./) los archivos para la solución del postwork de esta sesión. Están separados en tres carpetas que representan tres repositorios diferentes.