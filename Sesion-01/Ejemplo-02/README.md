# Ejemplo 02

## Instalación y configuración de AWS CLI

Antes de registrar su primera instancia, debe ejecutar la versión 1.16.180 de la AWS CLI o posterior en el equipo desde el que se ejecuta. Los detalles de la instalación dependen del sistema operativo de su estación de trabajo. 

Para comprobar la versión de la AWS CLI que está ejecutando, escriba ```aws --version``` en una sesión del shell.

La AWS CLI almacena esta información en un perfil (una colección de opciones) con el nombre `default` en el archivo credentials. De forma predeterminada, la información de este perfil se utiliza cuando se ejecuta un comando de la AWS CLI que no especifica explícitamente un perfil que se va a utilizar.

<pre><code>
aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
</code></pre>

## Crear claves de acceso en la consola AWS IAM

1.- Inicie sesión en la AWS Management Console y abra la consola de IAM en https://console.aws.amazon.com/iam/.

2.- En el panel de navegación, seleccione `Users`.

3.- Seleccione el nombre del usuario cuyas claves de acceso desee crear, y a continuación, elija la pestaña Security credentials (Credenciales de seguridad).

4.- En la sección `Access keys (Claves de acceso)`, haga clic en `Create access key (Crear clave de acceso)`.

5.- Para ver la nueva clave de acceso, elija `Show (Mostrar)`. No podrá obtener acceso de nuevo a la clave de acceso secreta cuando este cuadro de diálogo se cierre. Sus credenciales tendrán el aspecto siguiente:

<pre><code>
ID de clave de acceso: AKIAIOSFODNN7EXAMPLE
Clave de acceso secreta: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
</code></pre>

6.- Para descargar el par de claves, elija `Download .csv file (Descargar archivo .csv)`. Almacene las claves en un lugar seguro. No podrá obtener acceso de nuevo a la clave de acceso secreta cuando este cuadro de diálogo se cierre.

7.- Mantenga las claves en secreto para proteger su Cuenta de AWS y no las envíe nunca por correo electrónico. No las comparta fuera de su organización, aunque reciba una petición que parezca provenir de AWS o Amazon.com. Nadie que represente legítimamente a Amazon le pedirá nunca su clave secreta.

8.- Cuando descargue el archivo .csv, elija `Close (Cerrar)`. Cuando cree una clave de acceso, el par de claves se activa de forma predeterminada, y puede utilizar el par de inmediato.
