Electrum-XZC - Lightweight Zcoin client
=======================================

::

  Licence: MIT Licence
  Original Author: Thomas Voegtlin
  Language: Python
  Homepage: https://zcoin.io/






Getting started
===============

Electrum is a pure python application. If you want to use the
Qt interface, install the Qt dependencies::

    sudo apt-get install python3-pyqt5

If you downloaded the official package (tar.gz), you can run
Electrum from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum from its root directory, just do::

    ./electrum-xzc

You can also install Electrum on your system, by running this command::

    sudo apt-get install python3-setuptools
    python3 setup.py install

This will download and install the Python dependencies used by
Electrum, instead of using the 'packages' directory.

If you cloned the git repository, you need to compile extra files
before you can run Electrum. Read the next section, "Development
Version".



Development version
===================

ElectrumX developer decided to use newer Python 3 which isn't installed on many operating systems by default. Let's install it manually::

    sudo add-apt-repository ppa:jonathonf/python-3.6
    sudo apt-get update && sudo apt-get install python3.6 python3.6-dev python3-pip python3-pyqt5

To make python3 use the new installed python 3.6 instead of the default 3.5 release, run following 3 commands::

    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
    sudo update-alternatives --config python3

Install dependencies::

    sudo apt-get install pyqt5-dev-tools protobuf-compiler python-requests gettext
    pip3 install --upgrade pip setuptools wheel

Check out the code from Github::

    git clone git://github.com/zcoinofficial/electrum-xzc.git
    cd electrum-xzc

Install lyra2z lib::

    cd ./exlib/lyra2z-py/
    sudo python3 setup.py install
    cd ../../

Run install (this should install dependencies)::

    python3 setup.py install

Compile the icons file for Qt::

    pyrcc5 icons.qrc -o gui/qt/icons_rc.py

Compile the protobuf description file::

    protoc --proto_path=lib/ --python_out=lib/ lib/paymentrequest.proto

Create translations (optional)::

    ./contrib/make_locale




Creating Binaries
=================


To create binaries, create the 'packages' directory::

    ./contrib/make_packages

This directory contains the python dependencies used by Electrum.

Mac OS X / macOS
--------

See `contrib/build-osx/README`.


Windows
-------

See `contrib/build-wine/README` file.


Android
-------

See `gui/kivy/Readme.txt` file.
