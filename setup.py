from setuptools import find_packages, setup

setup(
    name='gsc_cli',
    version='1.7.0',
    author='FIXME',
    author_email='FIXME',
    description='FIXME',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='FIXME',
    packages=find_packages(),
    package_data={
        'gsc': ['templates/**/*', 'keys/**/*'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'docker',
        'jinja2',
        'tomli',
        'tomli_w',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'gsc=gsc.cli:main',
        ],
    },
)
