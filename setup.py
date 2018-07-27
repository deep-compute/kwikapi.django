from setuptools import setup, find_packages

from desc import get_long_description

long_description = get_long_description()

version = '0.2.5'
setup(
    name="kwikapi-django",
    version=version,
    packages=['kwikapi.django'],
    include_package_data=True,
    license='MIT License',  # example license
    description='Quickest way to build powerful HTTP APIs in Python',
    long_description=long_description,
    url='https://github.com/deep-compute/kwikapi.django',
    download_url="https://github.com/deep-compute/kwikapi.django/tarball/%s" % version,
    author='Deep Compute, LLC',
    author_email='contact@deepcompute.com',
    install_requires=[
    'django==1.11',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
