This is the collection of zamboni's pure-python dependencies.

From your zamboni root, do this::

    git clone --recursive git://github.com/jbalogh/zamboni-lib.git vendor

Sit back and relax while all that downloads, then proceed on your merry way.

To keep it up to date::

    pushd vendor && git pull && git submodule update --init && popd


How zamboni-lib was Made
------------------------

::

    pip install -I --install-option="--home=`pwd`/vendor" --src='vendor/src' -r requirements/dev.txt

    # ..delete some junk from vendor/lib/python...

    # Create the .pth file so Python can find our libs.
    # The first line gets all the normal packages.
    # The second line gets all the src packages.
    echo "import site; site.addsitedir('vendor/lib/python')" > zamboni.pth
    find src -type d -depth 1 >> zamboni.pth

    # Add all the submodules.
    for f in src/*; do
        pushd $f >/dev/null && REPO=$(git config remote.origin.url) && popd > /dev/null && git submodule add $REPO $f
    done
    git add .
