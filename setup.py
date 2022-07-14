from setuptools import setup
from setuptools import find_namespace_packages

# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    
    name='utils',
    packages = ['utils'],
    package_dir = {'utils': 'utils'},
    
    author='Akshay Raman',

    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version='0.1.0',
    
    description='Artificial Intelligence at the interface of Mathematics and Chemistry',
    long_description=long_description,
    long_description_content_type="text/markdown",

    url='https://github.com/ramanakshay/Optimal-Transport',
    

    # These are the dependencies the library needs in order to run.
    install_requires=[
        'numpy',
        'matplotlib',
    ],

    keywords='optimal transport, OT, DFT',

    # # here we specify any package data.
    # package_data={

    #     # And include any files found subdirectory of the "td" package.
    #     "td": ["app/*", "templates/*"],

    # },
    include_package_data=True,

    python_requires='>=3.7',

    classifiers=[
        
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',

        'Natural Language :: English',

        'Operating System :: OS Independent',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',

        'Topic :: Mathematics',
        'Topic :: Education',

    ]
)
