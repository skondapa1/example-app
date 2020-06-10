# Go parameters

prefix=$(shell bash -c pwd)
exec_prefix=$(GOPATH)
bindir=$(exec_prefix)/bin
datarootdir=$(prefix)/share
datadir=$(datarootdir)
mandir=$(datarootdir)/man


GOCMD=go1.13
GOARCH=386
GOBUILD=GOARCH=${GOARCH} $(bindir)/$(GOCMD) install 
GOCLEAN=$(bindir)/$(GOCMD) clean
GOTEST=$(bindir)/$(GOCMD) test
GOGET=$(bindir)/$(GOCMD) get

app=example-app-0.0.1

test: 
	$(GOTEST) -v ./...

.PHONY: download main

.DEFAULT_GOAL := all 

all: main

download:
	./go-setup.sh 
	dep init

main: 
	$(GOBUILD)  $(FLAGS) -v $(app)

install: main
	install -d ${DESTDIR}${PREFIX}/bin/
	install -m 755 $(bindir)/linux_386/$(app) ${DESTDIR}${PREFIX}/bin/$(app)

clean: 
	$(GOCLEAN)
	-rm -rf vendor
	-rm -rf _build
	-rm Gopkg.lock && rm Gopkg.toml

