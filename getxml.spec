%define name getxml
%define version 1.0.4
%define release %mkrel 8

Name:           %name
Summary:        XML file internationalization
Version:        %version
Release:        %release
Source:         %{name}-%{version}.tar.bz2
URL:            http://toutdoux.sourceforge.net
Group:          System/Libraries
BuildRoot:      %_tmppath/%name-buildroot
Buildrequires:	libxml-devel
License:	GPL

%description
XML File internationalization

%prep

%setup -q

%configure

%build

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,0755)
%doc AUTHORS README COPYING NEWS INSTALL ABOUT-NLS
%{_bindir}/*

