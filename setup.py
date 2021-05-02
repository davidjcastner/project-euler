# type: ignore

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='project_euler',
    version='0.0.0',
    author='David Castner',
    author_email='davidjcastner@gmail.com',
    description='personal solutions for Project Euler problems in python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/davidjcastner/project-euler',
    packages=setuptools.find_packages(),
    classifiers=[],
    python_requires='>=3.9',
)
