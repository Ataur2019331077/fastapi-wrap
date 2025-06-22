from setuptools import setup, find_packages

setup(
    name='fastapi-wrapper',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
    ],
    entry_points={
        'console_scripts': [
            'fastapi-wrapper = fastapi_wrapper.main:start'
        ]
    },
    author='Ataur Rahman',
    description='A simple FastAPI wrapper package',
    python_requires='>=3.7',
)
