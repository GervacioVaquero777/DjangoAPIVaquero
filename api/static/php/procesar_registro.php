<?php
class Registro {
    private $db; // Conexión a la base de datos

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    // Método para registrar un nuevo usuario
    public function registrarUsuario($nombre, $email, $password) {
        // Validar entradas (se puede agregar más validación según sea necesario)
        if (empty($nombre) || empty($email) || empty($password)) {
            return "Todos los campos son obligatorios.";
        }

        // Encriptar la contraseña
        $passwordHash = password_hash($password, PASSWORD_BCRYPT);

        // Preparar y ejecutar la consulta de inserción
        $query = "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)";
        $stmt = $this->db->prepare($query);

        if ($stmt) {
            $stmt->bind_param("sss", $nombre, $email, $passwordHash);
            if ($stmt->execute()) {
                return "Usuario registrado correctamente.";
            } else {
                return "Error al registrar al usuario.";
            }
        } else {
            return "Error en la preparación de la consulta.";
        }
    }
}
