DESTDIR=
PREFIX=/usr/local

all:
	echo "Only scripts."

install:
	mkdir -p ${DESTDIR}${PREFIX}/share/freewvs
	mkdir -p ${DESTDIR}${PREFIX}/bin
	install -t ${DESTDIR}${PREFIX}/share/freewvs freewvsdb/*.freewvs
	install -t ${DESTDIR}${PREFIX}/bin freewvs
	mkdir -p ${DESTDIR}/usr/share/locale/de_DE/LC_MESSAGES
	install i18n/de.mo ${DESTDIR}/usr/share/locale/de_DE/LC_MESSAGES/freewvs.mo
