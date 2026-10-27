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
        ('share/' + package_name + '/launch', ['launch/joystick_turtlesim.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mingyarrm',
    maintainer_email='mromer58@itam.mx',
    description='Control de Turtlesim con Joystick Comercial',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joy_turtle_controller = joystick_control.joy_turtle_controller:main'
        ],
    },
)
