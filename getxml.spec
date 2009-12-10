%define name getxml
%define version 1.0.4
%define release %mkrel 10

Name:           %name
Summary:        XML file internationalization
Version:        %version
Release:        %release
Source:         %{name}-%{version}.tar.bz2
URL:            http://toutdoux.sourceforge.net
Group:          System/Libraries
BuildRoot:      %_tmppath/%name-buildroot
Buildrequires:	libxml-devel libglib-devel
License:	GPLv2+

%description
XML File internationalization

%prep

%setup -q

%configure2_5x

%build

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

