import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_robot_description = get_package_share_directory('robot_description')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    # Exportar la ruta del modelo para que Gazebo Harmonic encuentre las mallas
    set_env = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=os.path.join(pkg_robot_description, '..')
    )

    urdf_file = os.path.join(pkg_robot_description, 'urdf', 'colmibot.urdf')
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        set_env,
        
        # 1. Iniciar servidor de Gazebo Harmonic con un piso vacío
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
            ),
            launch_arguments={'gz_args': '-r empty.sdf'}.items()
        ),
        
        # 2. Publicar la cinemática
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}]
        ),
        
        # 3. Inyectar el modelo URDF en Harmonic
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-topic', 'robot_description', '-name', 'colmibot'],
            output='screen'
        ),

        # 4. Puente matemático 
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=['/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist'],
            output='screen'
        ),
        
        # 5. Nodo del control físico
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[{'dev': '/dev/input/js2'}]
        ),
        
        # 6. Controlador redireccionado
        Node(
            package='joystick_control',
            executable='joy_turtle_controller',
            name='joy_turtle_controller',
            remappings=[('/turtle1/cmd_vel', '/cmd_vel')]
        )
    ])