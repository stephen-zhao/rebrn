import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='zhaostephen-rebrn',
    version='0.1.0',
    description='A CLI for bulk renaming files using dfregex search and replace.',

    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Stephen Zhao',
    author_email='mail@zhaostephen.com',

    url='https://github.com/stephen-zhao/rebrn',
    project_urls={
        "Source": "https://github.com/stephen-zhao/rebrn",
    },

    license='MIT',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],

    keywords=[
    ],

    package_dir={'': 'src'},
    packages=setuptools.find_namespace_packages(
        where='src',
        include=['zhaostephen.*'],
    ),
    entry_points={
        "console_scripts": [
            "rebrn=zhaostephen.rebrn._internal.cli.main:main",
        ]
    },

    python_requires='>=3.6',
    install_requires=[
        'datetime-matcher',
    ],
)
