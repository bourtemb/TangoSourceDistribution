
DOCS = tango-@DOCS_VER@.pdf
SUBDIRS = man

install-data-local:
	mkdir -p $(DESTDIR)/$(docdir)
	for file in $(DOCS); do \
	    cp -f $(srcdir)/$$file $(DESTDIR)/$(docdir)/$$file; \
		chmod u+w $(DESTDIR)/$(docdir)/$$file; \
	done;                                        

uninstall-local:
	for file in $(DOCS);do \
		rm $(DESTDIR)/$(docdir)/$$file; \
	done;

dist-hook:
	for file in $(DOCS); do        \
	   cp $(top_srcdir)/doc/$$file $(distdir)/$$file;       \
	done; \
	cp -R $(top_srcdir)/doc/src $(distdir); \
	rm -rf `find $(distdir) -name .svn`
