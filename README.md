# Representación Virtual: Colmibot (`robot_description`)

## Procedimiento, Herramientas y Recursos
Para generar la representación virtual del COLMIBOT, se exportaron los modelos tridimensionales de las piezas visuales y móviles esenciales desde el software CAD SolidWorks en formato `.stl`. Posteriormente, se creó el paquete `robot_description` en ROS 2 utilizando el formato URDF para definir la cinemática a través de eslabones y articulaciones. Finalmente, se utilizaron los nodos `robot_state_publisher` y `joint_state_publisher_gui` para la renderización visual en el simulador RViz2.

## Decisiones de Diseño y Simplificaciones
Se implementaron las siguientes simplificaciones geométricas justificadas en los objetivos de optimización del proyecto:
* **Colisiones primitivas:** En las etiquetas `<collision>` del código URDF, se omitieron las mallas `.stl` complejas y se utilizaron figuras primitivas geométricas (cajas). Esto reduce drásticamente la carga de cálculo del motor de físicas sin afectar el comportamiento del modelo[cite: 1].
* **Eliminación de detalles internos:** Se analizó el ensamble CAD completo y se determinó omitir la electrónica interna (Raspberry Pi 5, ESP32, BMS, baterías, cableado) y los motores mecánicos. Estos elementos no aportan al comportamiento cinemático exterior y su omisión reduce drásticamente la carga de polígonos, optimizando el rendimiento gráfico del simulador RViz.En el caso de la pieza Base.stl, en un inicio se vio como parte del ensamble esencial pero, posteriormente se decidio que no era relevante para la simplificación del modelo.
* **Reutilización de mallas:** La pieza `CLM-Llanta60mmD.stl` se exportó una sola vez y se reutilizó en el código para ambas ruedas motrices.

## Estructura del Paquete
Los archivos necesarios para cargar el modelo se organizaron dentro del paquete `robot_description` en el directorio `src` de la siguiente manera:

robot_description/
├── launch/
│   └── display.launch.py
├── meshes/
│   ├── CLM-Base.stl
│   ├── CLM-Body.stl
│   ├── CLM-Holder3TOF.stl
│   ├── CLM-Llanta60mmD.stl
│   ├── CLM-LogitechC920Montaj.stl
│   └── CLM-Plato.stl
├── rviz/
│   └── colmibot_view.rviz
├── urdf/
│   └── colmibot.urdf
├── package.xml
└── setup.py


## Comandos de Ejecución
Para compilar el espacio de trabajo y visualizar el modelo en RViz, se deben ejecutar los siguientes comandos en la terminal:

cd ~/colmibot_ws
colcon build --packages-select robot_description
source install/setup.bash
ros2 launch robot_description display.launch.py


## Problemas Encontrados y Soluciones
* **Divergencia de Escalas:** Al cargar las piezas, existía un conflicto de proporciones (metros vs. milímetros) desde SolidWorks. **Solución:** Se aplicó un factor de reducción con el atributo `scale="0.001 0.001 0.001"` en las etiquetas `<mesh>` del URDF y en otros casos la escala se dejo como `scale="1 1 1"`.
* **Error de visualización de mallas:** RViz no encontraba las rutas de los archivos `.stl`. **Solución:** Se utilizó la sintaxis estandarizada `package://robot_description/meshes/...` en el URDF y se registraron las carpetas correctamente en el archivo `setup.py`.

## Evidencia en Video
[https://drive.google.com/file/d/16IB0PjQeMRQKagOtvFkHJ7KSHSSlPe4R/view?usp=sharing]
