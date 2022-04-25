%define major 5
%define libname %mklibname KF5KDcraw %{major}
%define devname %mklibname KF5KDcraw -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	C++ interface around LibRaw library
Name:		libkdcraw
Version:	22.04.0
Release:	1
Epoch:		2
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
%rename	%{name}-common

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files
%doc README AUTHORS
%{_datadir}/qlogging-categories5/libkdcraw.categories

#----------------------------------------------------------------------

%define kdcraw_major 23
%define libkdcraw %mklibname kdcraw %{kdcraw_major}

%package -n %{libname}
Summary:	Kdcraw library
Group:		System/Libraries
Requires:	%{name}-common = %{EVRD}
Obsoletes:	%{_lib}kdcraw20 < 2:4.9.0
Obsoletes:	%{_lib}kdcraw21 < 2:4.10.0
Obsoletes:	%{_lib}kdcraw22 < 2:4.12.0
Obsoletes:	%{_lib}kdcraw23 < 2:15.12.0

%description -n %{libname}
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files -n %{libname}
%{_libdir}/libKF5KDcraw.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Conflicts:	kdegraphics4-devel < 2:4.6.90
Obsoletes:	libkdcraw-devel < 2:15.12.0

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devname}
%{_includedir}/KF5/KDCRAW
%{_includedir}/KF5/libkdcraw_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5KDcraw

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
