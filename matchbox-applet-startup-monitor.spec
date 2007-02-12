Summary:	Matchbox applet that provides feedback on application startup
Summary(pl.UTF-8):   Aplet środowiska Matchbox informujący o uruchamianiu aplikacji
Name:		matchbox-applet-startup-monitor
Version:	0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://projects.o-hand.com/matchbox/sources/mb-applet-startup-monitor/%{version}/mb-applet-startup-monitor-%{version}.tar.bz2
# Source0-md5:	ea4b3c1ebee3f731b77a2d4bf8e9aa3c
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	libmatchbox-devel
BuildRequires:	startup-notification-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Matchbox applet that provides feedback on application startup.

%description -l pl.UTF-8
Aplet środowiska Matchbox informujący o uruchamianiu aplikacji.

%prep
%setup -q -n mb-applet-startup-monitor-%{version}

%build
# not always defined when using recent xorg headers
CPPFLAGS="-DFALSE=0 -DTRUE=1"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mb-applet-startup-monitor
%{_pixmapsdir}/*.png
