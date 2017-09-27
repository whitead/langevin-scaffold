from distutils.core import setup

with open('README.md') as f:
    long_description = ''.join(f.readlines())

setup(name='LangevinSim',
      version='0.01',
      description='Langevin Simulator',
      long_description=long_description,
      author='Andrew White',
      packages=['lans'],
      entry_points=
      {
        'console_scripts': ['langevin=lans.lans:start']
      }
     )
