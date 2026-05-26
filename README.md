# Sistema de Gestión Académica - Control de Acceso

Este repositorio contiene el prototipo funcional de escritorio desarrollado para la asignatura **Análisis de Sistemas II (Ciclo I-2026)**. El objetivo principal es demostrar la implementación de controles de seguridad y segregación de funciones mediante un inicio de sesión estructurado por roles.

## 👥 Integrantes del Proyecto
* **Isaac Maldonado**
* **Tatiana Martínez** (Carnet: MC20008)

## 🔐 Procesos Clave Implementados
* **Control de Acceso (Login):** Validación de campos obligatorios y enrutamiento seguro según el rol seleccionado.
* **Seguridad Visual:** Ocultamiento de credenciales en pantalla utilizando enmascaramiento de caracteres (`show="*"`).
* **Vistas por Roles (RBAC):**
  * **Administrador:** Acceso completo al módulo de registro y control global de usuarios.
  * **Docente:** Interfaz para la gestión y edición de calificaciones y asistencia.
  * **Estudiante/Tutor:** Vista restringida de **solo lectura** para la consulta de récord de notas y porcentaje de asistencia.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Interfaz Gráfica:** Tkinter / TTK (Librería nativa)

## 🚀 Instrucciones de Ejecución
1. Asegúrate de tener instalado Python en tu equipo.
2. Descarga el archivo `Sistema_Academico.py` y el archivo `logo.png` en la misma carpeta.
3. Ejecuta el script desde la terminal o tu IDE favorito usando:
   ```bash
   python Sistema_Academico.py
