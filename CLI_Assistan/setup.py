from setuptools import setup, find_namespace_packages


setup(
    name='assistan',
    version='v.1.0.0',
    description='Command line personal helper. Working with contacts and sorting files in target directory',
    url='http://https://github.com/DmitriiMalii/CLI_Assistan',
    author='Dmitrii S Malii and misha_sid',
    author_email='dmitrii.malii@gmail.com, mishasydorchuk@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['assistan = assistan.main:main']}
)
