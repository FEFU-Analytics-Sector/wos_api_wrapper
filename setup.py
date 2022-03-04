import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="wos_api_wrapper",
    version="0.4.4",
    author="Aleksei Lepekha",
    author_email="lepehaleha@yandex.ru",
    description="Python package to access Web of Science API Expanded",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FEFU-Analytics-Sector/wos_api_wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests',
                      'simplejson'],
    python_requires='>=3.6',
)