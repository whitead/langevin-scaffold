from distutils.core import setup

with open('README.md') as f:
    long_description = ''.join(f.readlines())

# get the dependencies and installs
with open('requirements.txt') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(name='LangevinSim',
      version='0.01',
      description='Langevin Simulator',
      long_description=long_description,
      author='Andrew White',
      packages=['lans'],
      install_requires=install_requires,
      entry_points=
      {
        'console_scripts': ['langevin=lans.lans:start']
      }
     )
