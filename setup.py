from setuptools import setup
from setuptools import find_namespace_packages

# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    

    # Define the library name, this is what is used along with `pip install`.
    name='optimal',
    
#     packages = ['ot'],

#     package_dir = {'ot': 'ot'},
    
    packages=find_namespace_packages(where='ot'),
    
    package_dir={"": "ot"},

    # Define the author of the repository.
    author='Akshay Raman',

    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version='0.1.0',

    # Here is a small description of the library. This appears
    # when someone searches for the library on https://pypi.org/search.
    description='Artificial Intelligence at the interface of Mathematics and Chemistry',

    # I have a long description but that will just be my README
    # file, note the variable up above where I read the file.
    long_description=long_description,

    # This will specify that the long description is MARKDOWN.
    long_description_content_type="text/markdown",

    # Here is the URL where you can find the code, in this case on GitHub.
    url='https://github.com/ramanakshay/Optimal-Transport',
    

    # These are the dependencies the library needs in order to run.
    install_requires=[
        'numpy',
        'matplotlib',
    ],

    # Here are the keywords of my library.
    keywords='optimal transport, OT, DFT',

    # here are the packages I want "build."
#     packages=find_namespace_packages(
#         where=['ot', 'ot.*']
#     ),

    # # here we specify any package data.
    # package_data={

    #     # And include any files found subdirectory of the "td" package.
    #     "td": ["app/*", "templates/*"],

    # },

    # I also have some package data, like photos and JSON files, so
    # I want to include those as well.
    include_package_data=True,

    # Here I can specify the python version necessary to run this library.
    python_requires='>=3.7',

    # Additional classifiers that give some characteristics about the package.
    # For a complete list go to https://pypi.org/classifiers/.
    classifiers=[

        # I can say what phase of development my library is in.
        'Development Status :: 3 - Alpha',

        # Here I'll add the audience this library is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',

        # Here I'll define the license that guides my library.
        'License :: OSI Approved :: MIT License',

        # Here I'll note that package was written in English.
        'Natural Language :: English',

        # Here I'll note that any operating system can use it.
        'Operating System :: OS Independent',

        # Here I'll specify the version of Python it uses.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',

        # Here are the topics that my library covers.
        'Topic :: Mathematics',
        'Topic :: Education',

    ]
)
