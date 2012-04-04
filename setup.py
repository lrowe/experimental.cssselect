from setuptools import setup, find_packages

version = '0.3'
name = 'experimental.cssselect'
description = "Experimental version of lxml.cssselect"
install_requires = [
    'setuptools',
    'lxml',
    ]

setup(  
    name=name,
    version=version,
    description=description,
    long_description=open("README.txt").read() + "\n\n" +
                     open("CHANGES.txt").read(),
    author='Laurence Rowe',
    url='https://github.com/lrowe/experimental.cssselect',
    packages=find_packages('src'),
    package_dir={'':'src'},
    namespace_packages=[
        '.'.join(name.split('.')[:n+1]) for n in range(name.count('.'))],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    )
