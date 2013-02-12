from setuptools import setup

setup(
    name='galaxy-requirements-extractor',
    version='1.0',
    author='Julien Seiler <julien.seiler@coalkids.com>',
    py_modules=['extract_requirements'],
    description='',
    long_description='',
    license='BSD License',
    entry_points = {
        'console_scripts': ['extract-requirements = extract_requirements:main'],
    },
    install_requires=[]
)