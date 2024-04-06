from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Utilizing semi-supervised learning, specifically FixMatch, on medical data like X-ray images from ChestX-ray dataset. Enhancing model accuracy with ChexNet architecture for improved lung pathology classification.',
    author='Bartosz Latosek, Mateusz Krakowski',
    license='MIT',
)
