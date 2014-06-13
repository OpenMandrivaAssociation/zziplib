Summary:	ZZipLib - libZ-based ZIP-access Library
Name:		zziplib
%define	major	0
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname -d %{name}
Version:	0.13.60
Release:	10
License:	LGPL
Group:		System/Libraries
URL:		http://zziplib.sf.net
Source0:	http://prdownloads.sourceforge.net/zziplib/%{name}-%{version}.tar.bz2
Patch0:		zziplib-0.13.6-gcc46.patch
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	zlib-devel >= 1.1.4
# OE: python and pkgconfig is required for making the docs
BuildRequires:	python >= 2.3
BuildRequires:	pkgconfig
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:	zip

%description
zziplib provides read access to zipped files in a zip-archive,
using compression based solely on free algorithms provided by zlib.
zziplib provides an additional API to transparently access files
being either real files or zipped files with the same filepath argument.
This is handy to package many files being shared data into a single
zip file - as it is sometimes used with gamedata or script repositories.
The library itself is fully multithreaded, and it is namespace clean
using the zzip_ prefix for its exports and declarations.

%package -n     %{libname}
Summary:	ZZipLib - libZ-based ZIP-access Library
Group:		System/Libraries
Obsoletes:	%{name}
Provides:	%{name}
%rename		zziplib0

%description -n	%{libname}
zziplib provides read access to zipped files in a zip-archive,
using compression based solely on free algorithms provided by zlib.
zziplib provides an additional API to transparently access files
being either real files or zipped files with the same filepath argument.
This is handy to package many files being shared data into a single
zip file - as it is sometimes used with gamedata or script repositories.
The library itself is fully multithreaded, and it is namespace clean
using the zzip_ prefix for its exports and declarations.

%package -n     %{devname}
Summary:	ZZipLib - Development Files
Group:		Development/Other
%rename		zziplib0-devel
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig

%description -n	%{devname}
zziplib provides read access to zipped files in a zip-archive,
using compression based solely on free algorithms provided by zlib.
these are the header files needed to develop programs using zziplib.
there are test binaries to hint usage of the library in user programs.

%prep
%setup -q
%patch0 -p0

# perl path fix
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build
%setup_compile_flags
autoreconf -fi
%configure2_5x
%make

%check
make check

%install
%makeinstall_std

%multiarch_includes %{buildroot}%{_includedir}/zzip/_config.h

%multiarch_includes %{buildroot}%{_includedir}/zzip/_msvc.h

%files -n %{libname}
%doc ChangeLog README docs/COPYING*
%{_libdir}/libzzip*-*.so.*

%files -n %{devname}
%doc docs/README* docs/*.html ChangeLog README TODO
%{_bindir}/unzzip*
%{_bindir}/zz*
%{_bindir}/unzip-mem
%{_libdir}/libzzip*.so
%dir %{multiarch_includedir}/zzip
%{multiarch_includedir}/zzip/_config.h
%{multiarch_includedir}/zzip/_msvc.h
%{_includedir}/*.h
%dir %{_includedir}/zzip
%{_includedir}/zzip/*.h
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/*
