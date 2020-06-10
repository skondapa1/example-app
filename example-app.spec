
%define debug_package %{nil}
%global version 0.0.1

Name:           example-app
Version:        %{version}
Release:        1%{?dist}
Summary:        This application is an example for the golang binary RPM spec
License:        Proprietary 

#this file contains the contents of this directory, and is created by
#the build whenenver there is a ".write_tar" in the same directory as the
#spec file
Source0:        %{name}-%{version}.tar.gz
#Source1:        %{name}.service

BuildRequires:  golang 

# pull in golang libraries by explicit import path, inside the meta golang()
#Gorilla/mux is a popular package for writing web handlers. We’ll need this.
BuildRequires:  golang(github.com/gorilla/mux) >= 0-0.13

#Godotenv lets us read from a .env file that we keep in the root of our directory so we don’t have to hardcode things like our http ports. We’ll need this too.
BuildRequires:  golang(github.com/joho/godotenv) 

#Spew allows us to view structs and slices cleanly formatted in our console. This is nice to have
BuildRequires:  golang(github.com/davecgh/go-spew/spew) 

%description
# include your full description of the application here.

%prep
%autosetup -n %{name}-%{version}

rm -rf vendor

%build
# set up temporary build gopath, and put our directory there
mkdir -p ./_build/src/
#rsync -az --exclude=_build/ ./ ./_build/src/%{name}-%{version} 
ln -s $(pwd) ./_build/src/

export GOPATH=$(pwd)/_build 
cd ./_build/src/%{name}-%{version} 
./go-setup.sh 
dep init
make %{?_smp_mflags} VERSION=${RPM_PACKAGE_VERSION}


%install
export GOPATH=$(pwd)/_build 
export PATH=${GOPATH}:${PATH}
rm -rf %{buildroot}
cd ./_build/src/%{name}-%{version} 
make install DESTDIR=%{buildroot} PREFIX=/usr VERSION=${RPM_PACKAGE_VERSION}

%clean
rm -rf %{buildroot}

%check
export GOPATH=${PWD}/_build
export PATH=${GOPATH}:${PATH}
cd ./_build/src/%{name}-%{version} 
make test

%files
%{_bindir}/%{name}-%{version}

