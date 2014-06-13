%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	GNOME symbolic icons
Name:		gnome-icon-theme-symbolic
Version:	3.6.2
Release:	6
License:	CC-BY-SA
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-icon-theme-symbolic/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	icon-naming-utils >= 0.8.1
BuildRequires:	git-core
BuildRequires:	gtk+2.0
Requires:	gnome-icon-theme
Requires(post,postun):	gtk+2.0

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

./configure --prefix=%{_prefix} --enable-icon-mapping

%make

%install
%makeinstall_std GTK_UPDATE_ICON_CACHE=true

%files
%doc README COPYING NEWS AUTHORS
%{_iconsdir}/gnome/scalable/*/*

