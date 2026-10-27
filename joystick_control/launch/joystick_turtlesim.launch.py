from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Nodo del simulador
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),
        # Nodo oficial de ROS 2 que lee el control en tu puerto
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[{'dev': '/dev/input/js2'}]
        ),
        # Tu nodo controlador
        Node(
            package='joystick_control',
            executable='joy_turtle_controller',
            name='joy_turtle_controller'
        )
    ])
