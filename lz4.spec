#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lz4
Version  : 1.9.0
Release  : 24
URL      : https://github.com/lz4/lz4/archive/v1.9.0.tar.gz
Source0  : https://github.com/lz4/lz4/archive/v1.9.0.tar.gz
Summary  : extremely fast lossless compression algorithm library
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: lz4-bin = %{version}-%{release}
Requires: lz4-lib = %{version}-%{release}
Requires: lz4-license = %{version}-%{release}
Requires: lz4-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
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
providing compression speed > 500 MB/s per core,
scalable with multi-cores CPU.
It features an extremely fast decoder,
with speed in multiple GB/s per core,
typically reaching RAM speed limits on multi-core systems.

%package bin
Summary: bin components for the lz4 package.
Group: Binaries
Requires: lz4-license = %{version}-%{release}

%description bin
bin components for the lz4 package.


%package dev
Summary: dev components for the lz4 package.
Group: Development
Requires: lz4-lib = %{version}-%{release}
Requires: lz4-bin = %{version}-%{release}
Provides: lz4-devel = %{version}-%{release}
Requires: lz4 = %{version}-%{release}

%description dev
dev components for the lz4 package.


%package dev32
Summary: dev32 components for the lz4 package.
Group: Default
Requires: lz4-lib32 = %{version}-%{release}
Requires: lz4-bin = %{version}-%{release}
Requires: lz4-dev = %{version}-%{release}

%description dev32
dev32 components for the lz4 package.


%package lib
Summary: lib components for the lz4 package.
Group: Libraries
Requires: lz4-license = %{version}-%{release}

%description lib
lib components for the lz4 package.


%package lib32
Summary: lib32 components for the lz4 package.
Group: Default
Requires: lz4-license = %{version}-%{release}

%description lib32
lib32 components for the lz4 package.


%package license
Summary: license components for the lz4 package.
Group: Default

%description license
license components for the lz4 package.


%package man
Summary: man components for the lz4 package.
Group: Default

%description man
man components for the lz4 package.


%prep
%setup -q -n lz4-1.9.0
pushd ..
cp -a lz4-1.9.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555450671
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
make

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
make
popd

%install
export SOURCE_DATE_EPOCH=1555450671
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lz4
cp contrib/debian/copyright %{buildroot}/usr/share/package-licenses/lz4/contrib_debian_copyright
cp contrib/djgpp/LICENSE %{buildroot}/usr/share/package-licenses/lz4/contrib_djgpp_LICENSE
cp examples/COPYING %{buildroot}/usr/share/package-licenses/lz4/examples_COPYING
cp lib/LICENSE %{buildroot}/usr/share/package-licenses/lz4/lib_LICENSE
cp programs/COPYING %{buildroot}/usr/share/package-licenses/lz4/programs_COPYING
cp tests/COPYING %{buildroot}/usr/share/package-licenses/lz4/tests_COPYING
pushd ../build32/
%make_install32 PREFIX=/usr LIBDIR=/usr/lib64 PREFIX=/usr LIBDIR=/usr/lib32
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

%files dev32
%defattr(-,root,root,-)
/usr/lib32/liblz4.so
/usr/lib32/pkgconfig/32liblz4.pc
/usr/lib32/pkgconfig/liblz4.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblz4.so.1
/usr/lib64/liblz4.so.1.9.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/liblz4.so.1
/usr/lib32/liblz4.so.1.9.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lz4/contrib_debian_copyright
/usr/share/package-licenses/lz4/contrib_djgpp_LICENSE
/usr/share/package-licenses/lz4/examples_COPYING
/usr/share/package-licenses/lz4/lib_LICENSE
/usr/share/package-licenses/lz4/programs_COPYING
/usr/share/package-licenses/lz4/tests_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lz4.1
/usr/share/man/man1/lz4c.1
/usr/share/man/man1/lz4cat.1
/usr/share/man/man1/unlz4.1
