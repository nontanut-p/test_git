from setuptools import setup

package_name = 'turtlesim_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pat',
    maintainer_email='nontanut.c@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtlesim_control = turtlesim_control.turtlesim_control:main',
            'turtlesim_command = turtlesim_control.turtlesim_command:main',
            'test_subscribe =  turtlesim_control.test_subscribe:main' 
        ],
    },
)
