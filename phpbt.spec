Summary:	phpBugTracker is meant to be a replacement for Bugzilla
Summary(pl):	phpBugTracker - maj�cy by� zamiennikiem dla Bugzilli
Name:		phpbt
Version:	0.1.6
Release:	1
License:	GPL (?)
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
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

%description -l pl
phpBugTracker ma by� zamiennikiem dla Bugzilli. Jeszcze nim nie jest,
ale autor nad tym pracuje. Projekt wyr�s� z frustracji, kt�re
prze�ywa� autor pr�buj�c u�ywa� Bugzilli. Frustracje te wyznaczy�y
cele:
- prostota instalacji i u�ywania
- u�ywanie wzorc�w by uniezale�ni� wygl�d
- u�ywanie warstwy abstrakcji baz danych by uniezale�ni� od konkretnej
  bazy.

Projekt ma si� sta� przeno�nym i u�ytecznym rozwi�zaniem �ledzenia
b��d�w przez WWW.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/httpd/html/phpbt

cp -R * $RPM_BUILD_ROOT/home/httpd/html/phpbt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir /home/httpd/html/phpbt
/home/httpd/html/phpbt/*
