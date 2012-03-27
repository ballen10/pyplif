from distutils.core import setup
setup(name='PyPLIF',
    version='0.1a2',
    author='Muhammad Radifar',
    author_email='m.radifar05@gmail.com',
    packages=['pyplif'],
    package_data={'pyplif': ['LICENSE.txt', 'setup.sh']},
    url='http://code.google.com/p/pyplif/',
    description=['PyPLIF is a program/script written in Python to analyze protein-ligand interaction from the molecular docking result'],
    long_description=open('README.txt').read(),
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2',
    'Topic :: Scientific/Engineering :: Chemistry',
    ],
)