Name:           mpv-mpris
Version:        0.8.1
Release:        1%{?dist}
Summary:        MPRIS plugin for mpv

License:        MIT
URL:            https://github.com/hoyon/mpv-mpris
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  mpv-libs-devel
BuildRequires:  glib2-devel
BuildRequires:  pkg-config

Requires:       mpv

%description
mpv-mpris allows control of mpv using standard media keys

This plugin implements the MPRIS D-Bus interface and can
be controlled using tools such as playerctl or through
many Linux DEs, such as Gnome and KDE.

%prep
%autosetup

%build
%{set_build_flags}
%make_build

%install
mkdir -p %{buildroot}/%{_libdir}/mpv
mkdir -p %{buildroot}/%{_sysconfdir}/mpv/scripts/

install -p -m 0755 mpris.so %{buildroot}/%{_libdir}/mpv/mpris.so
ln -sf %{_libdir}/mpv/mpris.so %{buildroot}/%{_sysconfdir}/mpv/scripts/

%files
%dir %{_libdir}/mpv/
%{_libdir}/mpv/mpris.so
%dir %{_sysconfdir}/mpv/scripts
%{_sysconfdir}/mpv/scripts/mpris.so
%license LICENSE
%doc README.md

%changelog
* Sat Jun 18 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8.1-1
- update to version 0.8.1

* Fri Jun 17 2022 Jan Drögehoff <sentrycraft123@gmail.com> - 0.8-1
- update to version 0.8

* Mon Apr 11 2022 Leigh Scott <leigh123linux@gmail.com> - 0.7.1-1
- Updated to version 0.7.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Maxwell G <gotmax@e.email> - 0.6-1
- Updated to version 0.6

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.5-1
- Updated to version 0.5

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4-3
- change source

* Sat Jan 18 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4-2
- improve spec

* Fri Jan 17 2020 Jan Drögehoff <sentrycraft123@gmail.com> - 0.4-1
- Initial spec using version 4.0


