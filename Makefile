DESTDIR=
PREFIX=/usr/local

all:
	echo "Only scripts."

install:
	python3 setup.py install --prefix=${PREFIX}
	echo "WARNING: Makefile obsolete, please switch to setup.py"
