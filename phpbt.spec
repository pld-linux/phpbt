Summary:	phpBugTracker is meant to be a replacement for Bugzilla
Name:		phpbt
Version:	0.1.6
Release:	1
License:	GPL (?)
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://prdownloads.sourceforge.net/phpbt/%{name}-%{version}.tar.gz
URL:		http://phpbt.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phpBugTracker is meant to be a replacement for Bugzilla (one day).
It's obviously not there yet, but I'm working on it. This project grew
out of the frustrations I experienced in installing and using
bugzilla. Those frustrations inspired my design goals:

- Simplicity in use and installation
- Use templates to achieve presentation independence
- Use a database abstraction layer to achieve database independence

So this project will hopefully become a portable and powerful
web-based bug tracking solution.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
