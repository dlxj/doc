
RUNHASKELL = runhaskell Setup.lhs

SRCS = $(wildcard *.hs) $(wildcard Actor/*.hs)

all:	build

configure:
	$(RUNHASKELL) configure

build:
	$(RUNHASKELL) build

clean:
	$(RUNHASKELL) clean

run:
	dist/build/monao/monao

run-fullscreen:
	dist/build/monao/monao --fullscreen

doc:
	haddock -h -o man -l C:\\ghc\\haddock-2.0.0.0 -B c:\\ghc\\ghc-6.8.2 *.hs

imgs:
	$(RUNHASKELL) -itool tool/listup-imgs.hs data/img > Images.hs

count:
	@echo $(SRCS) | xargs -n1 echo | wc | gawk '{print $$1 " files";}'
	@cat $(SRCS) | wc | gawk '{print $$1 " lines";}'
