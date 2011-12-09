Name: mobipocket
Summary: A collection of plugins to handle mobipocket files
Version: 4.7.90
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
Conflicts: kdegraphics4-core < 2:4.6.90

%description
A collection of plugins to handle mobipocket files.

%files
%_kde_libdir/kde4/mobithumbnail.so
%_kde_libdir/strigi/strigila_mobi.so
%_kde_services/mobithumbnail.desktop

#----------------------------------------------------------------------

%prep
%setup -q


%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

