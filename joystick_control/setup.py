from setuptools import find_packages, setup

package_name = 'joystick_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/joystick_turtlesim.launch.py']), # Registra mi launch
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mingyarrm',
    maintainer_email='mingyarmedellin1998@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts' :
        [
            'joy_turtle_controller = joystick_control.joy_turtle_controller:main' # Registra mi nodo
        ],
    },
)
