from  setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='Mydemo',
    description=' Demo Mycode',
    long_description=readme(),
    long_description_content_typ='text/markdown',
    classifiers=[],
    url='',
    author='',
    author_email='huynhquoc1990@gmail.com',
    keyword='',
    license='MIT',
    packages=[],
    install_requires=[''],
    include_package_data=True,
    zip_safe=False
)
