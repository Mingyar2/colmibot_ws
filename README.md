# Práctica: Control de Turtlesim con Joystick Comercial

**Descripción de lo realizado:**
Se desarrolló un paquete en ROS 2 llamado `joystick_control` para teleoperar el simulador Turtlesim utilizando un control comercial (Xbox/PlayStation/Genérico) nativo en Ubuntu. El sistema se comunica a través del paquete oficial `joy`, identificando las entradas de los botones digitales y joysticks analógicos para generar comandos de velocidad espacial (`geometry_msgs/Twist`) hacia la tortuga.

**Decisiones tomadas:**
* **Mapeo de ejes:** Se asignó el eje 1 (palanca izquierda arriba/abajo) para la velocidad lineal y el eje 0 (palanca izquierda izquierda/derecha) para la velocidad angular, logrando un control intuitivo.
* **Inyección de puerto físico:** Se decidió inyectar el parámetro del puerto físico (ej. `/dev/input/js2`) directamente desde el archivo launch (`joystick_turtlesim.launch.py`) para evitar conflictos con las interfaces virtuales de VirtualBox.
* **Modos de velocidad (Mejora):** Se implementaron multiplicadores de velocidad asignados a los botones físicos (R1 para "Modo Turbo" y L1 para "Modo Precisión") para hacer el control más robusto y dinámico.

* Enlace de video en carpeta de seminario*
* https://drive.google.com/file/d/1bQa5RJuH_0bkw-OlDK1DOfgR2vXcCQPo/view?usp=drive_link

**Comandos utilizados para correr la actividad:**
```bash
# Compilar el espacio de trabajo
cd ~/colmibot_ws
colcon build
source install/setup.bash

# Iniciar el sistema completo (Simulador + Nodo Joy + Controlador)
ros2 launch joystick_control joystick_turtlesim.launch.py
