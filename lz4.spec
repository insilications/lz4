#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lz4
Version  : 1.7.5
Release  : 16
URL      : https://github.com/lz4/lz4/archive/v1.7.5.tar.gz
Source0  : https://github.com/lz4/lz4/archive/v1.7.5.tar.gz
Summary  : extremely fast lossless compression algorithm library
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: lz4-bin
Requires: lz4-lib
Requires: lz4-doc
BuildRequires : cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : valgrind

%description
LZ4 - Extremely fast compression
================================
LZ4 is lossless compression algorithm,
providing compression speed at 400 MB/s per core,
scalable with multi-cores CPU.
It features an extremely fast decoder,
with speed in multiple GB/s per core,
typically reaching RAM speed limits on multi-core systems.

%package bin
Summary: bin components for the lz4 package.
Group: Binaries

%description bin
bin components for the lz4 package.


%package dev
Summary: dev components for the lz4 package.
Group: Development
Requires: lz4-lib
Requires: lz4-bin
Provides: lz4-devel

%description dev
dev components for the lz4 package.


%package doc
Summary: doc components for the lz4 package.
Group: Documentation

%description doc
doc components for the lz4 package.


%package lib
Summary: lib components for the lz4 package.
Group: Libraries

%description lib
lib components for the lz4 package.


%prep
%setup -q -n lz4-1.7.5
pushd ..
cp -a lz4-1.7.5 build32
popd

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
make V=1

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32 PREFIX=/usr LIBDIR=/usr/lib64
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install PREFIX=/usr LIBDIR=/usr/lib64

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lz4
/usr/bin/lz4c
/usr/bin/lz4cat
/usr/bin/unlz4

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/liblz4.so
/usr/lib64/pkgconfig/liblz4.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblz4.so.1
/usr/lib64/liblz4.so.1.7.5
