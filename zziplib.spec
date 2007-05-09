%define	major 0
%define finalname %{name}%{major}

Summary:	ZZipLib - libZ-based ZIP-access Library
Name:		zziplib
Version:	0.13.49
Release:	%mkrel 1
License:	LGPL
Group:		System/Libraries
URL:		http://zziplib.sf.net
Source0:	http://prdownloads.sourceforge.net/zziplib/%{name}-%{version}.tar.bz2
Obsoletes:	%{name}
Provides:	%{name} %{name} = %{version}
BuildRequires:	autoconf2.5 >= 2.54
BuildRequires:	automake1.7
BuildRequires:	zlib-devel >= 1.1.4
# OE: python and pkgconfig is required for making the docs
BuildRequires:	python >= 2.3
BuildRequires:	pkgconfig
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:	zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
zziplib provides read access to zipped files in a zip-archive,
using compression based solely on free algorithms provided by zlib.
zziplib provides an additional API to transparently access files
being either real files or zipped files with the same filepath argument.
This is handy to package many files being shared data into a single
zip file - as it is sometimes used with gamedata or script repositories.
The library itself is fully multithreaded, and it is namespace clean
using the zzip_ prefix for its exports and declarations.

%package -n     %{finalname}
Summary:	ZZipLib - libZ-based ZIP-access Library
Group:		System/Libraries
Obsoletes:	%{name}
Provides:	%{name}

%description -n	%{finalname}
zziplib provides read access to zipped files in a zip-archive,
using compression based solely on free algorithms provided by zlib.
zziplib provides an additional API to transparently access files
being either real files or zipped files with the same filepath argument.
This is handy to package many files being shared data into a single
zip file - as it is sometimes used with gamedata or script repositories.
The library itself is fully multithreaded, and it is namespace clean
using the zzip_ prefix for its exports and declarations.

%package -n     %{finalname}-devel
Summary:	ZZipLib - Development Files
Group:		Development/Other
Obsoletes:	%{name}-devel
Provides:	%{name}-devel = %{version}
Requires:	%{finalname} = %{version}-%{release}
Requires:	pkgconfig

%description -n	 %{finalname}-devel
zziplib provides read access to zipped files in a zip-archive,
using compression based solely on free algorithms provided by zlib.
these are the header files needed to develop programs using zziplib.
there are test binaries to hint usage of the library in user programs.

%prep

%setup -q

# perl path fix
find -type f | xargs perl -pi -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%build

%configure2_5x

make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std 

%multiarch_includes %{buildroot}%{_includedir}/zzip/_config.h
%multiarch_includes %{buildroot}%{_includedir}/zzip/_msvc.h

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post -n %{finalname} -p /sbin/ldconfig

%postun -n %{finalname} -p /sbin/ldconfig

%files -n %{finalname}
%defattr(-,root,root)
%doc ChangeLog README docs/COPYING*
%{_libdir}/libzzip*-*.so.*

%files -n %{finalname}-devel
%defattr(-,root,root)
%doc docs/README* docs/*.html ChangeLog README TODO 
%{_bindir}/unzzip*
%{_bindir}/zz*
%{_bindir}/unzip-mem
%{_libdir}/libzzip*.la
%{_libdir}/libzzip*.so
%{_libdir}/libzzip*.a
%multiarch %{multiarch_includedir}/zzip/_config.h
%multiarch %{multiarch_includedir}/zzip/_msvc.h
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/*
