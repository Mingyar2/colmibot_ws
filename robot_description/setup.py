import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Rutas para copiar tus carpetas internas al instalar
        (os.path.join('share', package_name, 'launch'), glob('robot_description/launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('robot_description/urdf/*.urdf')),
        (os.path.join('share', package_name, 'meshes'), glob('robot_description/meshes/*.stl')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mingyar-rm',
    maintainer_email='mingyar-rm@todo.todo',
    description='Representacion virtual de Colmibot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
