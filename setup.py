from  setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='Mydemo',
    description=' Demo Mycode',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[],
    url='https://github.com/huynhquoc1990/Testthu.git',
    author='huynh tan Quoc',
    author_email='huynhquoc1990@gmail.com',
    keywords='',
    license='MIT',
    packages=[],
    install_requires=[''],
    include_package_data=True,
    zip_safe=False
)
