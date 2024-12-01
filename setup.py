from setuptools import setup, find_namespace_packages

setup(
    name='data-lib',
    version='0.1.0',
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'sqlalchemy>=1.4.0',
        'alembic>=1.7.0',
        'psycopg2-binary>=2.9.0',
    ],
    extras_require={
        'dev': [
            'pytest',
            'mypy',
        ]
    },
    python_requires='>=3.8',
)
