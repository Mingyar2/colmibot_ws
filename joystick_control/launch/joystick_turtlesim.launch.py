from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. Nodo del simulador
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),
        # 2. Nodo de lectura del control comercial (Apuntando al js2)
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[{'dev': '/dev/input/js2'}]  # <--- Aquí forzamos la lectura de tu control
        ),
        # 3. Tu nodo controlador matemático
        Node(
            package='joystick_control',
            executable='joy_turtle_controller',
            name='joy_turtle_controller'
        )
    ])
