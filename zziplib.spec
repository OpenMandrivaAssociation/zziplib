%bcond_with run_tests

Summary:	ZZipLib - libZ-based ZIP-access Library
Name:		zziplib
%define	major	13
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname -d %{name}
Version:	0.13.77
Release:	1
License:	LGPL
Group:		System/Libraries
URL:		http://zziplib.sf.net
Source0:	https://github.com/gdraheim/zziplib/archive/v%{version}.tar.gz
#Patch0:		zziplib-0.13.6-gcc46.patch
BuildSystem:	cmake
BuildRequires:	zlib-devel >= 1.1.4
BuildRequires:	xmlto
BuildRequires:	docbook-dtds
BuildRequires:	pkgconfig(sdl2)
# OE: python and pkgconfig is required for making the docs
BuildRequires:	python >= 2.3
BuildRequires:	pkgconfig
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
%if "%_lib" == "lib64"
%define depsuffix ()(64bit)
%else
%define depsuffix %{nil}
%endif
%rename		%{_lib}zziplib0
# For compatibility with previous autoconf-built package
Provides:	libzzip-0.so.%{major}%{depsuffix}
Provides:	libzzipfseeko-0.so.%{major}%{depsuffix}
Provides:	libzzipmmapped-0.so.%{major}%{depsuffix}
Provides:	libzzipwrap-0.so.%{major}%{depsuffix}

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

%install -a
# For compatibility with autoconf builds (used in old OM as
# well as current versions of some other distros)
cd %{buildroot}%{_libdir}
for i in *.so; do
	ln -s $(readlink $i) $(echo $i |cut -d. -f1)-0.so.13
	ln -s $i $(echo $i |cut -d. -f1)-0.so
done

%if %{with run_tests}
%check
%ninja_build -C build check
%endif

%files -n %{libname}
%doc ChangeLog README docs/COPYING*
%{_libdir}/libzzip*.so.*

%files -n %{devname}
%doc docs/README* ChangeLog README TODO
%{_bindir}/unzzip*
%{_bindir}/zz*
%{_bindir}/unzip-mem
%{_libdir}/libzzip*.so
%{_includedir}/*.h
%{_includedir}/zzip
%{_includedir}/SDL_rwops_zzip
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/zziplib
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/*
