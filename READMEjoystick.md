# Práctica: Control de Turtlesim con Joystick Comercial

**Descripción de lo realizado:**
Se desarrolló el paquete `joystick_control` en ROS 2 para teleoperar el simulador Turtlesim mediante un control comercial (Xbox/PlayStation/Genérico). El nodo controlador se suscribe a los datos físicos del paquete oficial `joy` y los traduce en comandos espaciales (`geometry_msgs/Twist`) hacia el tópico `/turtle1/cmd_vel`. Todo el sistema se orquesta mediante un archivo launch.

**Decisiones de diseño y funcionamiento:**
* **Velocidades Base:** Se establecieron velocidades máximas por defecto de 2.0 (lineal y angular) para evitar que el simulador se trabe.
* **Modos Multiplicadores (Mejora):** Se implementó una lectura directa de los botones superiores del control físico. Al mantener presionado **R1** (botón 5), se activa el **Modo Turbo** (multiplicador x2.0). Al presionar **L1** (botón 4), se activa el **Modo Precisión** (multiplicador x0.5 para maniobras finas).
* **Mapeo Cinemático:** Se asignó el eje 1 (palanca izquierda, arriba/abajo) para la velocidad lineal en X y el eje 0 (palanca izquierda, lados) para la velocidad angular en Z.

**Comandos utilizados para comprobación:**
```bash
cd ~/colmibot_ws
colcon build
source install/setup.bash
ros2 launch joystick_control joystick_turtlesim.launch.py
