Summary:	GUI front-end for hspell
Summary(pl.UTF-8):	Graficzny interfejs użytkownika do programu hspell
Name:		hspell-gui
Version:	0.2.6.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/hspell-gui/%{name}-%{version}.tar.bz2
# Source0-md5:	959dc62ada989e0d4ba127ce967b4e3a
URL:		http://hspell-gui.sourceforge.net/
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	hspell-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI front-end for hspell.

%description -l pl.UTF-8
Graficzny interfejs użytkownika do programu hspell.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/hspell-gui
%{_mandir}/man1/hspell-gui.1*
