import setuptools

setuptools.setup(
    name='Predators-and-Prey',
    version='0.1',
    author='dotereschenko',
    description='Predators-and-Prey',
    long_description_content_type="text/markdown",
    url='https://github.com/dotereschenko/Predators-and-Prey',
    license='MIT',
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=['opencv-python',
                      'Pillow',
                      'numpy',
                     ],
)
