from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='tianguix',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
    ],
    author='Carlos J. Hernandez',
    author_email='carlos3.14@gmail.com',
    description="'marketplace in a box' - a one-stop shop for all the essential infrastructure \
        and services needed to create a marketplace.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/CarlosJHdez/Tianguix',
    license="GNU Affero General Public License v3",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    project_urls={
            "Bug Tracker": "https://github.com/CarlosJHdez/Tianguix/issues",
            "Documentation": "https://tianguix.readthedocs.io/en/latest/",  # Replace with actual docs URL
            "Source Code": "https://github.com/CarlosJHdez/Tianguix",
        },
    python_requires='>=3.6',
)
