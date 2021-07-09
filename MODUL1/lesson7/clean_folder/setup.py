from setuptools import setup, find_namespace_packages


setup(
    name='clean_folder',
    version='v3_pathlib_only',
    description='Sorts and cleans the target directory',
    url='http://https://github.com/DmitriiMalii/clean_folder',
    author='Dmitrii S Malii',
    author_email='dmitrii.malii@gmail.com',
    license='PSF',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)
