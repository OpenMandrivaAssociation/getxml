%define name getxml
%define version 1.0.4
%define release %mkrel 10

Name:           %name
Summary:        XML file internationalization
Version:        %version
Release:        %release
Source0:        %{name}-%{version}.tar.bz2
# from GNU git
Source1:	config.sub.20091120
Source2:	config.guess.20091120
URL:            http://toutdoux.sourceforge.net
Group:          System/Libraries
BuildRoot:      %_tmppath/%name-buildroot
Buildrequires:	libxml-devel libglib-devel
License:	GPLv2+

%description
XML File internationalization

%prep

%setup -q
install -b %{SOURCE1} config.sub
install -b %{SOURCE2} config.guess

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,0755)
%doc AUTHORS README COPYING NEWS INSTALL ABOUT-NLS
%{_bindir}/*



%changelog
* Thu Dec 10 2009 Jérôme Brenier <incubusss@mandriva.org> 1.0.4-10mdv2010.1
+ Revision: 476081
- replace config.sub and config.guess by new version from GNU git
- move %%configure2_5x in the %%build section
- rebuild
- fix license tag
- $RPM_BUILD_ROOT -> %%{buildroot}

  + Thierry Vignaud <tvignaud@mandriva.com>
    - use %%configure2_5x
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.4-8mdv2009.0
+ Revision: 222602
- buildrequires libglib-devel instead of libglib2-devel
- buildrequires libglib2-devel
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- import getxml

  + Michael Scherer <misc@mandriva.org>
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Aug 10 2006 Lenny Cartier <lenny@mandriva.com> 1.0.4-6mdv2007.0
- rebuild

* Thu Jul 07 2005 Lenny Cartier <lenny@mandriva.com> 1.0.4-5mdk
- rebuild

* Wed Jun 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-4mdk
- rebuild

* Tue Apr 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-3mdk
- buildrequires

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-2mdk
- rebuild

* Thu Nov 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.4-1mdk
- needed for new toutdoux
