from setuptools import setup, find_packages

setup(
    name='job_processor',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas==1.3.3',
    ],
    entry_points={
        'console_scripts': [
            'job_processor = job_processor.main:main',
        ],
    },
)
