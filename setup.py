from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='asyncpgpromise',
    version='0.1.2',
    url='https://github.com/K-NRS/asyncpgpromise',
    author='Kerem Noras',
    author_email='kerem@noras.tech',
    description='pg-promise like wrapper for asyncpg',
    packages=find_packages(),    
    install_requires=['asyncpg'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
