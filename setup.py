import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='datalchemy',
    version='0.0.1',
    author='Manuel De Luzi',
    author_email='manueldeluzi@gmail.com',
    description='Embarks on a legendary data analysis quest with this magical data toolkit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mike-huls/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    },
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)
