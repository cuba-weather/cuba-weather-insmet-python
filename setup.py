from setuptools import setup

from cuba_weather_insmet import __version__

setup(
    name='cuba_weather_insmet',
    version=__version__,
    packages=[
        'cuba_weather_insmet',
        'cuba_weather_insmet/insmet_webparser',
        'cuba_weather_insmet/repositories',
    ],
    url='https://github.com/cuba-weather/cuba-weather-insmet-python',
    license='MIT',
    author='Cuban Open Source Community',
    description='Python3 client for (https://www.insmet.cu) weather API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['cuba-weather-municipality'],
)
