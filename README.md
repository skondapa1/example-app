#This is a sample app to show how to build go code and rpm with go1.13
#Built from ideas from : https://gist.github.com/jollyroger/f89c9a5954009a2254667e00ca0d0219

There are 2 ways to build..
  1. GOPATH has to be set to build using the Makefile. 
  2. rpmbuild -ba ./example-app.spec --build-in-place --nodeps


#To integrate with mock...
Use mock to build the .srpm: 
mock -r <chroot-name> --buildsrpm --spec example-app.spec --sources . --resultdir . This finishes without apparent issue.

Then use mock to build the binary RPM: 
mock -r <chroot-name> --rebuild <.src.rpm> --resultdir .
