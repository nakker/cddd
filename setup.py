from setuptools import setup

setup(
    name='cddd',
    version='1.2.2',
    packages=['cddd', 'cddd.data'],
    package_data={'cddd': ['data/*', 'data/default_model']},
    include_package_data=True,
    url='https://github.com/jrwnter/cddd',
    download_url='https://codeload.github.com/nakker/cddd/zip/refs/heads/master',
    license='MIT',
    author='Robin Winter',
    author_email='robin.winter@bayer.com',
    description='continous and data-driven molecular descriptors (CDDD)',
    python_requires='==3.8',
    install_requires=[
        'tensorflow-gpu==1.15.5',
        'scikit-learn',
        'pandas<=1.0.3',
        'requests',
        'appdirs'
      ],
    extras_require = {
        'cpu': [
            'tensorflow==1.15.5'
            ]
    },
    entry_points={
        'console_scripts': [
            'cddd = cddd.run_cddd:main_wrapper',
        ],
    },
)
