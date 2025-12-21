Summary:	XML file internationalization
Name:		getxml
Version:	1.0.4
Release:	12
License:	GPLv2+
Group:		System/Libraries
Url:		https://toutdoux.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
# from GNU git
Source1:	config.sub.20091120
Source2:	config.guess.20091120
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	pkgconfig(glib)
BuildRequires:	pkgconfig(libxml)

%description
XML File internationalization.

%files
%doc AUTHORS README COPYING NEWS INSTALL ABOUT-NLS
%{_bindir}/*

#----------------------------------------------------------------------------

%prep
%setup -q
install -b %{SOURCE1} config.sub
install -b %{SOURCE2} config.guess

%build
%configure2_5x
%make

%install
%makeinstall_std

