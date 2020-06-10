#!/bin/bash -f

# installs go1.13.3 

cmd="go"
$cmd version >/dev/null 2>&1 
status=$?

if [ $status -ne 0 ]; then
   echo "go is not present, Downloading go!!"
   wget https://dl.google.com/go/go1.13.3.linux-amd64.tar.gz
   sudo tar -xvf go1.13.3.linux-amd64.tar.gz
   sudo mv go /usr/local
   export GOROOT=/usr/local/go
   export PATH=$PATH\:${GOROOT}/bin
fi


export PATH=$PATH\:${GOPATH}/bin:$HOME/sdk/go1.13/bin:/usr/local/go
$cmd get golang.org/dl/go1.13
go1.13 download
sudo apt-get install go-dep
