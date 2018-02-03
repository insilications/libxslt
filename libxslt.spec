#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x15588B26596BEA5D (Daniel.Veillard@w3.org)
#
Name     : libxslt
Version  : 1.1.32
Release  : 34
URL      : http://xmlsoft.org/sources/libxslt-1.1.32.tar.gz
Source0  : http://xmlsoft.org/sources/libxslt-1.1.32.tar.gz
Source99 : http://xmlsoft.org/sources/libxslt-1.1.32.tar.gz.asc
Summary  : Library providing the GNOME XSLT engine
Group    : Development/Tools
License  : MIT
Requires: libxslt-bin
Requires: libxslt-lib
Requires: libxslt-doc
BuildRequires : docbook-xml
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-python
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : python-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev
Patch1: 0004-Make-generate-id-deterministic.patch

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package bin
Summary: bin components for the libxslt package.
Group: Binaries

%description bin
bin components for the libxslt package.


%package dev
Summary: dev components for the libxslt package.
Group: Development
Requires: libxslt-lib
Requires: libxslt-bin
Provides: libxslt-devel

%description dev
dev components for the libxslt package.


%package doc
Summary: doc components for the libxslt package.
Group: Documentation

%description doc
doc components for the libxslt package.


%package lib
Summary: lib components for the libxslt package.
Group: Libraries

%description lib
lib components for the libxslt package.


%prep
%setup -q -n libxslt-1.1.32
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517685549
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517685549
rm -rf %{buildroot}
%make_install
## make_install_append content
find -name "*.pyo" %{buildroot} | xargs rm -f
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/xsltConf.sh

%files bin
%defattr(-,root,root,-)
/usr/bin/xslt-config
/usr/bin/xsltproc

%files dev
%defattr(-,root,root,-)
/usr/include/libexslt/exslt.h
/usr/include/libexslt/exsltconfig.h
/usr/include/libexslt/exsltexports.h
/usr/include/libxslt/attributes.h
/usr/include/libxslt/documents.h
/usr/include/libxslt/extensions.h
/usr/include/libxslt/extra.h
/usr/include/libxslt/functions.h
/usr/include/libxslt/imports.h
/usr/include/libxslt/keys.h
/usr/include/libxslt/namespaces.h
/usr/include/libxslt/numbersInternals.h
/usr/include/libxslt/pattern.h
/usr/include/libxslt/preproc.h
/usr/include/libxslt/security.h
/usr/include/libxslt/templates.h
/usr/include/libxslt/transform.h
/usr/include/libxslt/variables.h
/usr/include/libxslt/xslt.h
/usr/include/libxslt/xsltInternals.h
/usr/include/libxslt/xsltconfig.h
/usr/include/libxslt/xsltexports.h
/usr/include/libxslt/xsltlocale.h
/usr/include/libxslt/xsltutils.h
/usr/lib64/libexslt.so
/usr/lib64/libxslt.so
/usr/lib64/pkgconfig/libexslt.pc
/usr/lib64/pkgconfig/libxslt.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libxslt/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libexslt.so.0
/usr/lib64/libexslt.so.0.8.20
/usr/lib64/libxslt.so.1
/usr/lib64/libxslt.so.1.1.32
