import os
from setuptools import setup, find_packages


setup(
    name='Magellan Sync',
    version='0.1.0',
    author='Hyyudu',
    author_email='hyyudu@gmail.com',
    description='Терминал синхронизации',
    entry_points={
        # 'console_scripts': [
        #     'partner-programs=partner_programs.cli:cli',
        # ],
    },
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    extras_require={
        'test': [
            'diff-cover',
            'mock==2.0.0',
            'pycodestyle==2.3.1',
            'pylint==1.8.1',
            'pytest==3.0.7',
            'pytest-cov==2.5.1',
            'pytest-mock==1.6.0',
        ],
    },
)
