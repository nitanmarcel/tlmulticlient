from setuptools import setup

setup(
    name='tlmulticlient',
    version='0.0.5',
    #url='https://github.com/nitanmarcel/tlmulticlient',
    license='MIT',
    author='Nitan Alexandru Marcel',
    author_email='nitan.marcel@protonmail.com',
    description='Multi Sessions addon for Telethon',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    packages=['tlmulticlient'],
    platforms='any',
    install_requires=['telethon'],
    include_package_data=True,
    project_urls={
        'Donations': 'https://paypal.me/marcelalexandrunitan?locale.x=en_US',
        'Source': 'https://github.com/nitanmarcel/tlmulticlient'
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    keywords='telethon telegram telegram-client'
)
