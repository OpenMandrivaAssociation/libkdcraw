#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

%define major 5
%define oldlib5name %mklibname KF5KDcraw %{major}
%define lib5name %mklibname KF5KDcraw
%define dev5name %mklibname KF5KDcraw -d
%define libname %mklibname KDcrawQt6
%define devname %mklibname KDcrawQt6 -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	C++ interface around LibRaw library
Name:		libkdcraw
Version:	26.04.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		System/Libraries
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/libkdcraw/-/archive/%{gitbranch}/libkdcraw-%{gitbranchd}.tar.bz2#/libkdcraw-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%rename	%{name}-common
%rename plasma6-%{name}

%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%install -a
# Install the LibRaw cmake module -- the KDcrawQt6 module references it,
# but it isn't provided anywhere else
mkdir -p %{buildroot}%{_libdir}/cmake/Modules
cp cmake/modules/* %{buildroot}%{_libdir}/cmake/Modules/

%files
%doc README AUTHORS
%{_datadir}/qlogging-categories6/libkdcraw.categories

#----------------------------------------------------------------------
%package -n %{libname}
Summary:	Kdcraw library for Qt 6.x
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
# Not really, but something has to get rid of the prehistoric package
Obsoletes:	%{lib5name} < %{EVRD}

%description -n %{libname}
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%files -n %{libname}
%{_libdir}/libKDcrawQt6.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Devel stuff for %{name} for Qt 6.x
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
# Not really, but something has to get rid of the prehistoric package
Obsoletes:	%{dev5name} < %{EVRD}

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devname}
%{_includedir}/KDcrawQt6
%{_libdir}/libKDcrawQt6.so
%{_libdir}/cmake/KDcrawQt6
%{_libdir}/cmake/Modules/FindLibRaw.cmake
