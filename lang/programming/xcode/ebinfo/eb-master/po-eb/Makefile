# Makefile for program source directory in GNU NLS utilities package.
# Copyright (C) 1995, 1996, 1997 by Ulrich Drepper <drepper@gnu.ai.mit.edu>
#
# This file file be copied and used freely without restrictions.  It can
# be used in projects which are not available under the GNU Public License
# but which still want to provide support for the GNU gettext functionality.
# Please note that the actual code is *not* freely available.

## Note that the following macros must be set by your hand.
top_builddir = ..
subdir = po-eb

TEXTDOMAIN = eb
POFILES = ja.po
MOFILES = ja.mo
POTFILES = \
	$(top_srcdir)/eb/error.c 
## end

PACKAGE = eb
VERSION = 4.4.3

SHELL = /bin/sh

srcdir = .
top_srcdir = ..

prefix = /usr/local
datarootdir = ${prefix}/share
datadir = ${datarootdir}
localedir = $(datadir)/locale

mkdir_p = $(top_builddir)/./install-sh -c -d
INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644
mkinstalldirs = $(install_sh) -d
install_sh = $(SHELL) /Users/vvw/Desktop/eb-master/install-sh

MSGFMT = :
XGETTEXT = :
MSGMERGE = msgmerge

DISTFILES = Makefile.in $(TEXTDOMAIN).pot $(MOFILES) $(POFILES)

.SUFFIXES:
.SUFFIXES: .po .pox .mo

.po.pox:
	$(MAKE) $(TEXTDOMAIN).pot
	$(MSGMERGE) $< $(srcdir)/$(TEXTDOMAIN).pot -o $*.pox

.po.mo:
	file=$(srcdir)/`echo $* | sed 's,.*/,,'`.mo \
	  && rm -f $$file && $(MSGFMT) -o $$file $<

all: all-no

all-yes: $(MOFILES)
all-no:

$(TEXTDOMAIN).pot: $(POTFILES)
	$(XGETTEXT) --default-domain=$(TEXTDOMAIN) --add-comments \
	   --keyword=_ --keyword=N_ $(POTFILES) \
	&& test ! -f $(TEXTDOMAIN).po \
	   || ( rm -f $(srcdir)/$(TEXTDOMAIN).pot \
		&& mv $(TEXTDOMAIN).po $(srcdir)/$(TEXTDOMAIN).pot )

install: install-exec install-data
install-exec:
install-data: install-data-no
install-data-no: all
install-data-yes: all
	$(mkinstalldirs) $(DESTDIR)$(datadir)
	@catalogs='$(MOFILES)'; \
	for cat in $$catalogs; do \
	  cat=`echo $$cat | sed 's/^.*\/\([^\/]*\)$$/\1/'` ; \
	  lang=`echo $$cat | sed 's/\.mo$$//'`; \
	  dir=$(localedir)/$$lang/LC_MESSAGES; \
	  $(mkinstalldirs) $(DESTDIR)$$dir; \
	  if test -r $$cat; then \
	    $(INSTALL_DATA) $$cat $(DESTDIR)$$dir/$(TEXTDOMAIN).mo; \
	    echo "installing $$cat as" \
		 "$(DESTDIR)$$dir/$(TEXTDOMAIN).mo"; \
	  else \
	    $(INSTALL_DATA) $(srcdir)/$$cat \
	      $(DESTDIR)$$dir/$(TEXTDOMAIN).mo; \
	    echo "installing $(srcdir)/$$cat as" \
		 "$(DESTDIR)$$dir/$(TEXTDOMAIN).mo"; \
	  fi; \
	done

# Define this as empty until I found a useful application.
installcheck:

uninstall:
	catalogs='$(MOFILES)'; \
	for cat in $$catalogs; do \
	  cat=`echo $$cat | sed 's/^.*\/\([^\/]*\)$$/\1/'` ; \
	  lang=`echo $$cat | sed 's/\.mo$$//'`; \
	  rm -f $(DESTDIR)$(localedir)/$$lang/LC_MESSAGES/$(TEXTDOMAIN).mo; \
	done
	rm -f $(DESTDIR)$(gettextsrcdir)/po-Makefile.in

check: all

dvi info tags TAGS ID:

mostlyclean:
	rm -f core core.* *.pox $(TEXTDOMAIN).po *.old.po
	rm -fr *.o

clean: mostlyclean

distclean: clean
	rm -f Makefile *.mo

maintainer-clean: distclean
	@echo "This command is intended for maintainers to use;"
	@echo "it deletes files that may require special tools to rebuild."
	rm -f *.mo

distdir = $(top_builddir)/$(PACKAGE)-$(VERSION)/$(subdir)
dist distdir: update-po $(DISTFILES)
	dists="$(DISTFILES)"; \
	for file in $$dists; do \
	  ln $(srcdir)/$$file $(distdir) 2> /dev/null \
	    || cp -p $(srcdir)/$$file $(distdir); \
	done

update-po: Makefile
	$(MAKE) $(TEXTDOMAIN).pot
	cd $(srcdir); \
	catalogs='$(MOFILES)'; \
	for cat in $$catalogs; do \
	  cat=`echo $$cat | sed 's/^.*\/\([^\/]*\)$$/\1/'` ; \
	  lang=`echo $$cat | sed 's/\.mo$$//'`; \
	  mv $$lang.po $$lang.old.po; \
	  echo "$$lang:"; \
	  if $(MSGMERGE) $$lang.old.po $(TEXTDOMAIN).pot -o $$lang.po; then \
	    rm -f $$lang.old.po; \
	  else \
	    echo "msgmerge for $$cat failed!"; \
	    rm -f $$lang.po; \
	    mv $$lang.old.po $$lang.po; \
	  fi; \
	done

Makefile: Makefile.in $(top_builddir)/config.status
	cd $(top_builddir) && CONFIG_FILES=$(subdir)/$@ CONFIG_HEADERS= \
	  $(SHELL) ./config.status

# Tell versions [3.59,3.63) of GNU make not to export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
