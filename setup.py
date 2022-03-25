import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='datalchemy',
    version='0.0.4',
    author='Manuel De Luzi',
    author_email='manueldeluzi@gmail.com',
    description='Embarks on a legendary data analysis quest with this magical data toolkit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mandel94/datalchemy',
    license='MIT',
    packages=['datalchemy'],
    install_requires=['pandas', 'numpy'],
)
