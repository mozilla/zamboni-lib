This is the collection of zamboni's pure-python dependencies.

From your zamboni root, do this::

    git clone --recursive git://github.com/jbalogh/zamboni-lib.git vendor

Sit back and relax while all that downloads, then proceed on your merry way.

To keep it up to date::

    pushd vendor && git pull && git submodule update --init && popd
