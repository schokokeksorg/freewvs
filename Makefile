DESTDIR=
PREFIX=/usr/local

all:
	echo "Only scripts."

install:
	mkdir -p ${DESTDIR}${PREFIX}/share/freewvs
	mkdir -p ${DESTDIR}${PREFIX}/bin
	install -t ${DESTDIR}${PREFIX}/share/freewvs freewvsdb/*.freewvs
	install -t ${DESTDIR}${PREFIX}/bin freewvs
