from setuptools import setup, find_packages


version = __import__('dirtyedit').__version__

setup(
  name = 'django-dirtyedit',
  packages=find_packages(),
  include_package_data=True,
  version = version,
  description = ' Django application to edit files from the admin interface',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-dirtyedit', 
  download_url = 'https://github.com/synw/django-dirtyedit/releases/tag/'+version, 
  keywords = ['django', 'editor'], 
  classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  install_requires=[
        'dirtyedit',
        'ckeditor',
        'codemirror2',
        'reversion'
    ],
  zip_safe=False
)
