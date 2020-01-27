# This Makefile is only for cleaning up the directory and making backups.

clean:
	rm -f *~ *.log *.dvi *.ans *.inx *.bnx sources.tex
	mkdir tmpsave
	mv galley.tex cover.tex front.tex cont.tex rear.tex tmpsave
	rm -f galley.* cover.* front.* cont.* rear.*
	mv tmpsave/* .
	rmdir tmpsave
	rm -f pref.ref ans.ref cred.ref index.ref

floppy:
	-mkdir /tmp/gkp
	rm -f /tmp/gkp/*
	cp *.tex /tmp/gkp
	compress /tmp/gkp/*
	bar cvf /dev/rfd0 /tmp/gkp/*
	bar tvf /dev/rfd0
	eject


