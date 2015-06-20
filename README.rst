sphinxcontrib-gravatar is a Sphinx extension for Gravatar

|travis| |coveralls| |downloads| |version| |license| |requires|

Features
========
* Provide ``gravatar icon`` for your document.

Set up
======
Make environment with pip::

  $ pip install sphinxcontrib-gravatar

Usage
=====
setup conf.py with::

  # set extension
  extensions += ['sphinxcontrib.gravatar']

  # define gravatar users
  gravatar_users = (
      ('tell-k', {'email': 'ffk2005@gmail.com' }),
  )

write gravatar role::

  .. gravatar:: tell-k

  # If you wanted to write in the text. you can use "Substitution References".

  .. |tell-k-gravatar| gravatar:: tell-k

  my gravatar image |tell-k-gravatar|.

and run::

    $ make html

Option
============

TODO more documented.

conf.py options::

  gravatar_default_size = 30
  gravatar_default_image = "http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50"
  gravatar_default_rating = "pg"
  gravatar_default_target = "http://github.com/tell-k/"
  gravatar_force_default = True
  gravatar_force_refresh = True
  gravatar_unlink = True
  gravatar_default_class = "custom-classname"

  gravatar_users = (
      ('tell-k', {
          'email': 'ffk2005@gmail.com',
          'default': 'http://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50',
          'force_default': True,
          'unlink': True,
          'target': "http://github.com/tell-k/",
          'rating': "pg",
          'class': u"custom-classname",
          'alt': "alternative text",
      }),
  )

Directive options::

 .. gravatar:: tell-k
    :size: 200
    :default: mm
    :target: http://github.com/tell-k
    :rating: pg
    :class: test-gravatar
    :alt: altnativetext


Requirement
===========
* Python 2.7 or later.
* Sphinx 1.2.x or later.

Using
===========
* `Gravatar APIs <http://en.gravatar.com/site/implement/>`_ .

License
=======
* sphinxcontrib-gravatar Licensed under the BSD License.

See the LICENSE file for specific terms.

.. |travis| image:: https://travis-ci.org/tell-k/sphinxcontrib-gravatar.svg?branch=master
    :target: https://travis-ci.org/tell-k/sphinxcontrib-gravatar

.. |coveralls| image:: https://coveralls.io/repos/tell-k/sphinxcontrib-gravatar/badge.png
    :target: https://coveralls.io/r/tell-k/sphinxcontrib-gravatar
    :alt: coveralls.io

.. |requires| image:: https://requires.io/github/tell-k/sphinxcontrib-gravatar/requirements.svg?tag=v0.1.1
     :target: https://requires.io/github/tell-k/sphinxcontrib-gravatar/requirements/?tag=v0.1.1
     :alt: requires.io

.. |downloads| image:: https://img.shields.io/pypi/dm/sphinxcontrib-gravatar.svg
    :target: http://pypi.python.org/pypi/sphinxcontrib-gravatar/
    :alt: downloads

.. |version| image:: https://img.shields.io/pypi/v/sphinxcontrib-gravatar.svg
    :target: http://pypi.python.org/pypi/sphinxcontrib-gravatar/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/sphinxcontrib-gravatar.svg
    :target: http://pypi.python.org/pypi/sphinxcontrib-gravatar/
    :alt: license
