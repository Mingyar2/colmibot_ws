---

## Integración del Gemelo Digital en Gazebo Harmonic y Teleoperación

**Descripción breve de la actividad:**
En esta práctica se realizó la transición de la representación cinemática estática en RViz hacia una simulación física dinámica utilizando **Gazebo Harmonic** en ROS 2 Jazzy. Se integró el control por hardware (joystick) desarrollado en prácticas anteriores para teleoperar el robot dentro del entorno simulado, orquestando todo mediante un único archivo *launch* y estableciendo un puente de comunicación entre ROS 2 y Gazebo.

### Procedimiento, Herramientas y Recursos
* **Simulador:** Se utilizó Gazebo Harmonic, la versión nativa compatible con ROS 2 Jazzy.
* **Puente de comunicación:** Se empleó el paquete `ros_gz_bridge` para traducir los mensajes estándar de ROS 2 (`geometry_msgs/msg/Twist`) al formato nativo de Gazebo (`gz.msgs.Twist`).
* **Control Físico:** Se integraron los nodos del paquete `joystick_control` (`joy_node` y el controlador matemático) para enviar comandos espaciales al robot simulado.

### Decisiones de Diseño y Modificaciones al URDF
Para lograr que el COLMIBOT interactuara correctamente con la física del simulador, se implementaron las siguientes adiciones en el archivo `colmibot.urdf`:
1. **Propiedades Inerciales (`<inertial>`):** Se calcularon y añadieron las masas y matrices de inercia (ixx, iyy, izz) para el chasis y las llantas. Sin esto, el motor de físicas de Gazebo ignoraría el modelo.
2. **Colisiones Primitivas (`<collision>`):** Se descartaron las mallas `.stl` complejas para el cálculo de choques y se utilizaron primitivas geométricas:
   * **Cilindros** para las llantas, rotados 90 grados en X para que su banda de rodadura toque el suelo.
   * Una **Caja** para el chasis principal, desplazada 5 cm hacia arriba (Z=0.05) para evitar que el modelo atravesara el suelo y levantara las ruedas.
3. **Plugin Diferencial:** Se integró el plugin oficial `gz::sim::systems::DiffDrive` para Gazebo Harmonic, configurando la separación de las ruedas (`0.22 m`), el radio (`0.03 m`) y el tópico de escucha (`cmd_vel`).

### Arquitectura de Nodos y Comunicación (`rqt_graph`)
El sistema está orquestado por el archivo `gazebo_colmi.launch.py`. El flujo de datos es el siguiente:
1. `joy_node` captura las señales del control USB y publica en `/joy`.
2. `joy_turtle_controller` se suscribe a `/joy`, procesa los ejes y publica comandos espaciales. Mediante *remapping* en el launch, la salida `/turtle1/cmd_vel` se redirige a `/cmd_vel`.
3. `parameter_bridge` intercepta `/cmd_vel` en ROS 2 y lo envía a la red de Gazebo.
4. El plugin `DiffDrive` en Gazebo recibe el comando y aplica torque físico a las llantas del modelo.

### Comandos de Ejecución y Comprobación
```bash
# 1. Iniciar la simulación y el control simultáneamente
ros2 launch robot_description gazebo_colmi.launch.py

# 2. Comprobación de red (en una nueva terminal)
ros2 node list
ros2 topic list
rqt_graph
```

### Problemas Encontrados y Soluciones
1. **Error de rutas de mallas en Gazebo (`Unable to find file`):** Gazebo Harmonic no lograba resolver las rutas usando la macro `$(find...)`. **Solución:** Se restauró la sintaxis estándar `package://robot_description/meshes/...` en el URDF y se exportó la variable de entorno `GZ_SIM_RESOURCE_PATH` directamente desde el archivo de *launch*.
2. **Llantas "acostadas" y robot flotando (Efecto trineo):** Una doble rotación en las etiquetas visuales provocaba que los cilindros de las ruedas actuaran como pilares, y el centro de colisión del chasis atravesaba el piso. **Solución:** Se reajustaron los ejes respetando el eje Y nativo de las mallas `.stl` y se elevó exclusivamente la caja de colisión del chasis (`Z=0.05 m`).

### Evidencia en Video
[INSERTA AQUÍ TU ENLACE AL VIDEO DE YOUTUBE O DRIVE - Máximo 3 minutos]