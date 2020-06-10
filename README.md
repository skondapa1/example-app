#This is a sample app to show how to build go code and rpm with go1.13
#Built from ideas from : https://gist.github.com/jollyroger/f89c9a5954009a2254667e00ca0d0219

To build the app and the rpm - 
  1. rpmbuild -ba ./example-app.spec --build-in-place --nodeps

You can also build with just running make..
  1. The current directory 'example_app' must be under <src_tree>/src
  2. GOPATH has to be set to <src_tree>
  3. run ./go-setup.sh to download go1.13 and download all the dependencies using 'dep init'
  4. make

#To integrate with mock...
Use mock to build the .srpm: 
mock -r <chroot-name> --buildsrpm --spec example-app.spec --sources . --resultdir . This finishes without apparent issue.

Then use mock to build the binary RPM: 
mock -r <chroot-name> --rebuild <.src.rpm> --resultdir .
