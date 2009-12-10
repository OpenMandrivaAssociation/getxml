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

