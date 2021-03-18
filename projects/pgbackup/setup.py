from setuptools import find_packages, setup

with open("README.md", "r") as f:
    description = f.read()

setup(
    name ="pgbackup",
    version="0.1.0",
    description="A utility to backup Postgresql databases",
    url="https://github.com/edinomoniz/sixmonthpython",
    packages=find_packages("src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: System :: Archiving :: Backup",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={'': 'src'},
    install_requires=['boto3'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ],
    }
)
