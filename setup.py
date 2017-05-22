from setuptools import setup
# TODO: Write me

setup(name='tfstudio',
      version = '0.0',
      description = 'TensorFlow Studio',
      long_description = 'TensorFlow model and data management tool',
      url = 'https://github.com/ilblackdragon/studio',
      packages = ['studio'],
      install_requires = [
        'tensorflow',
        'apscheduler',
        ],
      scripts=['studio/studio-runner'],
      include_package_data=True,
      zip_safe = False)



