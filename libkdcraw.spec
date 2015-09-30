%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	C++ interface around LibRaw library
Name:		libkdcraw
Version:	15.08.1
Release:	2
Epoch:		2
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	automoc4
BuildRequires:	kdelibs4-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libraw)

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files
%doc README AUTHORS NEWS TODO COPYING

#----------------------------------------------------------------------

%package common
Summary:	Non-library files for the kdcraw library
Group:		System/Libraries

%description common
Common files for the kdcraw library

%files common
%{_kde_appsdir}/libkdcraw
%{_kde_iconsdir}/hicolor/*/apps/kdcraw.png

#------------------------------------------------

%define kdcraw_major 23
%define libkdcraw %mklibname kdcraw %{kdcraw_major}

%package -n %{libkdcraw}
Summary:	Kdcraw library
Group:		System/Libraries
Requires:	%{name}-common = %{EVRD}
Obsoletes:	%{_lib}kdcraw20 < 2:4.9.0
Obsoletes:	%{_lib}kdcraw21 < 2:4.10.0
Obsoletes:	%{_lib}kdcraw22 < 2:4.12.0

%description -n %{libkdcraw}
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files -n %{libkdcraw}
%{_kde_libdir}/libkdcraw.so.%{kdcraw_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkdcraw} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_includedir}/libkdcraw/
%{_kde_libdir}/libkdcraw.so
%{_kde_libdir}/pkgconfig/libkdcraw.pc

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
