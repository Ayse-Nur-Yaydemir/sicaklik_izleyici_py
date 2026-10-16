from setuptools import find_packages, setup

package_name = 'sicaklik_izleyici_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aysenuryaydemir',
    maintainer_email='aysenuryaydemir@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
                    'sensor = sicaklik_izleyici_py.sensor:main',
                    'sicaklik_yayinci = sicaklik_izleyici_py.sicaklik_yayinci:main',
        ],
    },
)
