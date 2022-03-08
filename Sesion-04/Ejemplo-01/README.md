# Ejemplo 1 - Modelos de diseño de microservicios con Azure

## Objetivos 🎯

* Analizar bloque a bloque el diagrama de arquitectura en Azure.

## Desarrollo 📝

<img src="../assets/azure-microservices-patterns.png">

El patrón [Ambassador](https://docs.microsoft.com/es-es/azure/architecture/patterns/ambassador) se puede usar para la descarga de tareas comunes de conectividad de cliente, como la supervisión, el registro, el enrutamiento, la seguridad (por ejemplo, TLS) de una manera independiente del lenguaje. Los servicios de Ambassador se suelen implementar como un sidecar (consulte a continuación).

El patrón [Anti-Corruption Layer](https://docs.microsoft.com/es-es/azure/architecture/patterns/anti-corruption-layer) implementa una fachada entre aplicaciones nuevas y heredadas para garantizar que el diseño de una nueva aplicación no está limitado por dependencias en sistemas heredados.

El patrón [Backends for Frontends](https://docs.microsoft.com/es-es/azure/architecture/patterns/backends-for-frontends) crea servicios de back-end independientes para distintos tipos de clientes, como equipos de escritorio y móviles. De este modo, no es necesario que un único servicio de back-end controle los requisitos conflictivos de varios tipos de cliente. Este patrón puede ayudar a mantener cada microservicio simple gracias a la separación de problemas específicos del cliente.

El patrón [Bulkhead](https://docs.microsoft.com/es-es/azure/architecture/patterns/bulkhead) aísla los recursos críticos, como el grupo de conexiones, la memoria y la CPU, para cada carga de trabajo o servicio. Al usar patrones Bulkhead, una sola carga de trabajo (o servicio) no puede consumir todos los recursos, lo que privaría a otros. Este patrón aumenta la resistencia del sistema al evitar los errores en cascada causados por un servicio.

[Agregación de puertas de enlace](https://docs.microsoft.com/es-es/azure/architecture/patterns/gateway-aggregation) agrega solicitudes a varios microservicios individuales en una sola solicitud, lo que reduce el intercambio de mensajes entre los consumidores y los servicios.

[Descarga con puertas de enlace](https://docs.microsoft.com/es-es/azure/architecture/patterns/gateway-offloading) permite que cada microservicio descargue la funcionalidad de servicio compartido, como el uso de certificados SSL, a una puerta de enlace de API.

[Enrutamiento de puerta de enlace](https://docs.microsoft.com/es-es/azure/architecture/patterns/gateway-routing) enruta las solicitudes a varios microservicios mediante un único punto de conexión para que los consumidores no tengan que administrar muchos puntos de conexión independientes.

[Sidecar](https://docs.microsoft.com/es-es/azure/architecture/patterns/sidecar) implementa componentes de una aplicación auxiliar como un proceso o contenedor independiente para proporcionar aislamiento y encapsulación.

[Strangler Fig](https://docs.microsoft.com/es-es/azure/architecture/patterns/strangler-fig) admite la refactorización incremental de una aplicación mediante el reemplazo gradual de funciones específicas por servicios nuevos.

Para obtener el catálogo completo de modelos de diseño en la nube en el Centro de arquitectura de Azure, consulte [Modelos de diseño en la nube](https://docs.microsoft.com/es-es/azure/architecture/patterns/).
