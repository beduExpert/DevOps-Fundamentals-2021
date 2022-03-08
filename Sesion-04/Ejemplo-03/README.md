# Ejemplo 3. Arquitectura de Microservicios con AWS Lambdas

## Objetivos 🎯

* Analizar bloque a bloque el diagrama de arquitectura en AWS con Lambdas.

## Desarrollo 📝

En este artículo me centraré en explicar el funcionamiento de Lambda a través de un ejemplo concreto y cómo nos podría ayudar a migrar aplicaciones monolíticas en sendas plataformas en la nube basadas en arquitecturas de microservicios.

Un poco de teoría (que siempre ayuda)

Lambda se basa en un concepto de computación en la nube denominado Serverless. ¿qué significa esto?

Básicamente Serverless es sin servidor. El serverless computing o la arquitectura serverless es un modelo en la nube que permite a los usuarios crear y ejecutar aplicaciones y procesos sin entrar en contacto con el servidor. Por lo tanto, a pesar de su denominación, estos entornos en la nube también cuentan con servidores, con la diferencia de que es el proveedor (Amazon en este caso) el que se encarga de suministrarlo, gestionarlo y escalarlo. Serverless es parte de lo que se conoce como [Plataformas como Servicios (PaaS)](https://azure.microsoft.com/es-es/overview/what-is-paas/).

La ventaja de este tipo de arquitectura en la nube es evidente, nos permite centrarnos en el desarrollo del producto y la ejecución del software, más que en la infraestructura capaz de soportar este desarrollo. Podemos ponerle más atención a la lógica de negocios de nuestra aplicación, sin embargo, desde el mismo código debemos agregar instrucciones adicionales como las funciones sin estado y todas aquellas instrucciones acerca de cómo debe reaccionar un programa a determinados eventos. Debido precisamente al papel esencial que juegan las funciones, hay proveedores que ofrecen sus servicios serverless bajo el nombre “Function as a Service (FaaS)” y acá es donde entra Lambda de Amazon AWS.

    Los proveedores de serverless computing no solo son los responsables de que los recursos de servidor necesarios estén siempre disponibles, sino también de garantizar el mayor nivel de seguridad y alta disponibilidad posible. Por norma general, estos servicios suelen facturarse según el modelo de pago por uso o Pay per Use, de manera que los clientes solo tienen que pagar por los servicios de los que de hecho han disfrutado.

    HTTPS://AWS.AMAZON.COM/ES/SERVERLESS/

<img src="../assets/aws-architecture-diagram-lambdas.jpg"  style="background-color: white">

<p align = "center"><i>
Patrón arquitectónico para microservicios con Lambda. Fuente: Amazon AWS. https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/microservices-with-lambda.html
El patrón de arquitectura de microservicio no está vinculado a la arquitectura típica de tres capas (3 tiers); sin embargo, este patrón popular puede obtener importantes beneficios del uso de recursos sin servidor.</i></p><br>

En esta arquitectura, cada uno de los componentes de la aplicación se desacopla y se implementa y opera de forma independiente. Una API creada con Amazon API Gateway y funciones ejecutadas posteriormente por AWS Lambda es todo lo que necesita para construir un microservicio. El equipo de desarrollo es libre de utilizar estos servicios para desacoplar y fragmentar su entorno al nivel de granularidad deseado.

En general, un entorno de microservicios puede presentar las siguientes dificultades: sobrecarga repetida para crear cada nuevo microservicio, problemas con la optimización de la densidad / utilización del servidor, complejidad de ejecutar múltiples versiones de múltiples microservicios simultáneamente y proliferación de requisitos de código del lado del cliente para integrar los servicios de forma separada.

Cuando se crean microservicios utilizando recursos sin servidor, estos problemas se vuelven más fáciles de resolver y, en algunos casos, simplemente desaparecen. El patrón de microservicios sin servidor reduce la barrera para la creación de cada microservicio posterior (Amazon API Gateway incluso permite la clonación de API existentes y el uso de funciones Lambda en otras cuentas -tal y como se aprecia en la imagen-). La optimización de la utilización del servidor ya no es relevante con este patrón de arquitectura.
