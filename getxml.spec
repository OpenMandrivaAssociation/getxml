%define name getxml
%define version 1.0.4
%define release 10

Name:		getxml
Summary:	XML file internationalization
Version:	1.0.4
Release:	10
License:	GPLv2+
Group:		System/Libraries
Url:		http://toutdoux.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
# from GNU git
Source1:	config.sub.20091120
Source2:	config.guess.20091120
Buildrequires:	libxml-devel
Buildrequires:	libglib-devel

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
%makeinstall

%files 
%doc AUTHORS README COPYING NEWS INSTALL ABOUT-NLS
%{_bindir}/*

