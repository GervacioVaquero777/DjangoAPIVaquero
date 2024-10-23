<?php
require 'conexion.php'; // Archivo donde tienes tu conexión a la base de datos
require 'RecuperarPassword.php'; // Archivo donde está definida la clase RecuperarPassword

// Obtener la conexión
$conexion = new mysqli('localhost', 'usuario', 'contraseña', 'basedatos');

// Instanciar la clase RecuperarPassword
$recuperarPassword = new RecuperarPassword($conexion);

// Obtener el email del formulario
$email = $_POST['email'];

// Llamar al método para enviar el enlace de recuperación
$resultado = $recuperarPassword->enviarEnlaceRecuperacion($email);

// Mostrar el resultado
echo $resultado;
?>
