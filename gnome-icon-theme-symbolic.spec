Summary: GNOME symbolic icons
Name: gnome-icon-theme-symbolic
Version: 2.91.0
Release: %mkrel 1
License: CC-BY-SA
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: icon-naming-utils >= 0.8.1
BuildRequires: git-core
#BuildRequires: inkscape
BuildArch: noarch
Requires: gnome-icon-theme
Requires(post): gtk+2.0
Requires(postun): gtk+2.0

%description
Purpose of this icon theme is to extend the base icon theme that
follows the Tango style guidelines for specific purposes. This would
include OSD messages, panel system/notification area, and possibly
menu icons.

Icons follow the naming specification, but have a -symbolic suffix, so
only applications specifically looking up these symbolic icons will
render them. If a -symbolic icon is missing, the app will fall back to
the regular name.

%prep
%setup -q

%build

./configure --prefix=%_prefix --enable-icon-mapping

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std GTK_UPDATE_ICON_CACHE=true

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING NEWS AUTHORS
%{_datadir}/icons/gnome/scalable/*/*
