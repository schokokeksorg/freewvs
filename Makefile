DESTDIR=
PREFIX=/usr/local

all:
	echo "Only scripts."

install:
	mkdir -p ${DESTDIR}/var/lib/freewvs
	mkdir -p ${DESTDIR}${PREFIX}/bin
	install -t ${DESTDIR}/var/lib/freewvs freewvsdb/*.json
	install -t ${DESTDIR}${PREFIX}/bin freewvs
