# Sesión 5: Integración y entrega continua 🤖

## 1. Objetivos 🎯

- Descubrir herramientas de CI
- Familiarizarse con la instalación y configuración de Jenkins
- Conocer los plugins básicos
- Utilizar los plugins en los projectos.

## 2. Contenido 📘
⏱️ 10 minutos

Como ya hemos visto en el prework, Jenkins es una herramienta muy popular pero no es la única en el mercado, todas ellas trabajan de formas similares, ofreciendo pros y contras, diferentes y con una experiencia de usuario única.

En este curso exploramos Jenkins por ser una de las mas populares, pero también por que nos da buenas báses para explorar alternativas.

Analicemos algunas de las herramientas populares de CI/CD disponibles en el mercado y te invitamos a visitar su sitio web.

### [Jenkins](https://www.jenkins.io/)

Jenkins es un servidor CI basado en Java. Ha ido más allá de los límites de un simple servidor CI y es popular en el mercado como servidor de automatización de código abierto.

Características clave:

Jenkins puede funcionar como un servidor CI independiente o una plataforma de entrega continua para prácticamente cualquiera de sus proyectos
Los paquetes prediseñados para Unix, Windows y OS X garantizan un proceso de instalación fácil
Una interfaz web disponible para su uso en la configuración rápida del servidor
Implementable en una red de máquinas, lo que mejora el rendimiento de compilaciones y pruebas
Participación de una gran comunidad con marcas de software líderes en el desarrollo
Costo: código abierto

Cubriremos esta herramienta con más detalle en secciones posteriores.

### [Travis CI](https://www.travis-ci.com/)

Travis CI automatiza el proceso de prueba de software y la implementación de aplicaciones. Está construido como una plataforma que se integra con sus proyectos de GitHub para que pueda comenzar a probar su código sobre la marcha.

Características clave:

Gratis para público código abierto proyectado en GitHub
Es simple registrarse, agregar un proyecto y comenzar a probar
Soporte bilingüe para que su código funcione sin problemas en todas las versiones
Verificación de solicitud de extracción automatizada
Funciona con correo electrónico, Slack, HipChat y otros para notificaciones sencillas
Herramientas extendidas de API y CMD para administración personalizada
Costo: Gratis para repositorios abiertos, Enterprise para privados

### [TeamCity](https://www.jetbrains.com/teamcity/)

TeamCity es una solución de servidor CI inteligente de Jetbrains, para cualquier tamaño de entorno de software. Como herramienta de CI/CD, TeamCity tiene como objetivo mejorar los lanzamientos. Además, la herramienta brinda la capacidad de ejecutar compilaciones paralelas en diferentes plataformas y entornos, simultáneamente.
El tablero de TeamCity está basado en un navegador y proporciona información sobre el estado del proyecto y los informes para los usuarios.

Características clave:

Gran soporte para Visual Studio; control de versiones de herramientas, pruebas de marco, cobertura de código, análisis de código, todo incluido sin scripts externos
La configuración es reutilizable, por lo que se puede evitar el esfuerzo de duplicación en la escritura de código, todo gracias a una base intuitiva
Control integral de versiones para estructurar su proyecto
Informes de historial detallados para compilaciones, fallas y cualquier cambio adicional realizado
Costo: Gratis, Negocios Desde $299

### [CircleCI](https://circleci.com/)

CircleCI proporciona una plataforma de vanguardia para la integración y la entrega, que ha ayudado a varios equipos de todo el mundo a publicar su código a través de la automatización de compilaciones, la automatización de pruebas y un proceso de implementación integral.

Características clave:

Primero puede crear una cuenta, luego agregar un proyecto y comenzar a construir. La plataforma toma la configuración personalizada de su código directamente
Se integra bien con Maven, Gradle y otras herramientas de compilación de primer nivel
Perfecta integración con AWS, Heroku, Google Cloud y otros
Costo: Gratis, Premium A partir de $50

### [CI de GitLab](https://docs.gitlab.com/ee/ci/)

GitLab es una plataforma de gestión de código de rápido crecimiento. Proporciona muchas herramientas desde un solo tablero, lo que ayuda en la gestión de problemas, vistas de código, integración e implementación continuas, todo dentro de un solo tablero. Desde el principio hasta las etapas de producción, obtienes una vista panorámica de cómo crece y madura tu proyecto, con GitLab.

Características clave:

Integrado directamente en el flujo de trabajo de GitLab
Agregue máquinas adicionales para escalar sus pruebas de rendimiento
Con los scripts de compilación de CMD, puede programarlos en cualquier idioma
Pruebas de versiones personalizadas para verificar sucursales individualmente
Implementación manual y capacidades de reversión sin esfuerzo
Costo: Gratis para Community Edition, Enterprise A partir de $16 por usuario

### [Bamboo](https://www.atlassian.com/software/bamboo)

Bamboo es un servidor de implementación e integración continua desarrollado por Atlassian. Bamboo une compilaciones, pruebas y lanzamientos automatizados en un solo flujo de trabajo mediante la integración con otros productos de Atlassian, como JIRA, Bitbucket, Stash, Hipchat y Confluence.
Bamboo utiliza los conceptos de agentes para realizar todas las tareas de CI-CD, incluidas la creación, la prueba y la implementación. Hay dos tipos de agentes:

Agentes locales (se ejecutan como parte del servidor de Bamboo como su proceso)
Agentes remotos (ejecutar en cualquier otro servidor y computadora)
Características clave:

Use Bamboo con su pila favorita, incluidos Docker, AWS y S3; funciona de inmediato con su lenguaje de codificación favorito
Proyectos de implementación personalizados para archivar el historial de cada una de sus versiones de lanzamiento
Solucione errores críticos rápidamente usando agentes personalizados que se pueden asignar para compilaciones inmediatas
Esquema detallado de su historial de código antes de la implementación, lo que lo ayuda a comprender el progreso que está logrando
Compatible con Bitbucket y JIRA para una experiencia integral de CI
Con permisos por entorno, los desarrolladores y el control de calidad pueden implementar en sus propios entornos a pedido mientras la producción permanece bloqueada.
Costo: $10 para equipos pequeños; $800 para equipos en crecimiento

### [Cruise Control](http://cruisecontrol.sourceforge.net/)

CruiseControl es un marco de código abierto construido con Java que supervisa su proceso de construcción continuo. Proporciona un panel web flexible para ver los detalles de sus compilaciones. Los desarrolladores pueden ampliar su flujo de trabajo más allá de la funcionalidad básica, utilizando complementos.

Características clave:

Bucle de compilación personalizado para ciclos de compilación
Informes JSP para administrar los resultados de compilación
Interfaz GUI para ver la salida de las compilaciones
Costo: código abierto

### [Spinnaker](https://spinnaker.io/)

Una plataforma de entrega continua multinube de código abierto para lanzar cambios de software rápidos con confianza, Spinnaker es una herramienta segura y altamente configurable para acelerar el desarrollo y aprovecha las mejores prácticas de la industria desde el primer momento.

Características clave:

Se integra con una variedad de proveedores de nube
Se integra con Jenkins y Travis
Soporte para mensajería a través de Slack, correo electrónico y más
Gestión de clústeres
Gestión de implementación
Costo: código abierto

---

## 3. Actividad 1: Conociendo los Plugins de Jenkins.
⏱️ 15 minutos

Jenkins por sí mismo, es funcional, pero hay una gran candidad de plugins que facilitan la experiencia de uso. En esta activadad el instructor explicará brevemente cada plugin de la lista de los que instalamos en prework. Cabe señalar que todo lo que se hace por via de plug-ins se puede hacer via script, solo que los plugins nos facilitan el trabajo.

---

## 4. Reto 1: Crear un usuario en Jenkins.
⏱️ 10 minutos

>Dirígete a la página del [Reto 1](./Reto-01)

---

## 5. Reto 2: Configura variables de entorno globales.
⏱️ 10 minutos

>Dirígete a la página del [Reto 2](./Reto-02)

---
## 6. Reto 3: Automatizar el inicio del projecto via SCM.
⏱️ 10 minutos

>Dirígete a la página del [Reto 3](./Reto-03)

---
## 7. Reto 4: Habilitar la comunicación del contenedor Jenkins con el Docker del host.
⏱️ 20 minutos

>Dirígete a la página del [Reto 4](./Reto-04)

---
## 9. Ejemplo 1: Comprobando comunicaciónes entre dos contenedores.
⏱️ 5 minutos

>Dirígete a la página del [Ejemplo 1](./Ejemplo-01)

---

## 10. Postwork 📝

Encuentra las indicaciones y consejos para reflejar los avances de tu proyecto de este módulo.

- [**`POSTWORK SESIÓN 5`**](./Postwork/)
