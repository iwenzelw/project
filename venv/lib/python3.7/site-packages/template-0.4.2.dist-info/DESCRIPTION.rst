Template
########

.. image:: https://travis-ci.org/adarnimrod/template.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/template

A CLI tool for generating files from Jinja2 templates and environment
variables.

Examples
--------

.. code:: shell

    $ template -h
    usage: template [-h] [-o OUTPUT] [filename]

    A CLI tool for generating files from Jinja2 templates and environment
    variables.

    positional arguments:
      filename              Input filename

      optional arguments:
        -h, --help            show this help message and exit
          -o OUTPUT, --output OUTPUT
                                  Output to filename
    $ export name='John'
    $ echo 'Hello {{ name if name is defined else 'world' }}. | template
    Hello John.
    $ echo '{{ USER }}' > username.j2
    $ template --output username.txt username.j2
    $ cat username.txt
    John


Jinja filters
-------------

The following Jinja filters were added:

- :code:`to_yaml`: Convert to yaml.
- :code:`from_yaml`: Convert from yaml.
- :code:`to_json`: Convert to json.
- :code:`from_json`: Convert from json.
- :code:`combine`: Combine 2 dictionaries.
- :code:`to_toml`: Convert to toml.
- :code:`from_toml`: Convert from toml.
- :code:`jmespath`: Queries data using the `JMESPath <http://jmespath.org/>`_
  query language.

Example usage can be seen in :code:`tests.sh` and for specific filters in the
docstrings in :code:`template/filters.py`.

Testing
-------

Tests require Python 2.7, Python 3.3 or later and Tox and are run by running
:code:`tox`. Also, Travis CI is used to test on multiple Python versions for
every push.

Release
-------

Releases require Python 2.7 or Python 3.3 or later and Tox. To release a new
version bump the version in the :code:`VERSION` file and run :code:`tox -e
release`.

License
-------

This software is licensed under the AGPL 3+ license (see the :code:`LICENSE.txt`
file).

Author
------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.

TODO
----

- Fix test failure on Python 3.2
  (https://travis-ci.org/adarnimrod/template/jobs/194581463).
- Release on tagged commits to PyPI in Travis CI
  (https://docs.travis-ci.com/user/deployment/pypi/ and
  https://docs.travis-ci.com/user/encryption-keys/).


