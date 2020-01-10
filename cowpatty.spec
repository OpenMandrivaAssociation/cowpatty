%define debug_package %{nil}

Name:		cowpatty
Summary:	Brute-force dictionary attack against WPA-PSK
Version:	4.6
Release:	2
Source0:	http://wirelessdefence.org/Contents/Files/%{name}-%{version}.tgz
Patch0:		cowpatty-4.6-parallel-build.patch
Group:		Networking/Other
URL:		http://cowpatty.sf.net
BuildRequires:	openssl-devel
BuildRequires:	libpcap-devel
License:	GPLv2

%description
coWPAtty is designed to audit the pre-shared key (PSK) selection for WPA
networks based on the TKIP protocol. Supply a libpcap file that includes the
TKIP four-way handshake to mount an offline dictionary attack with a supplied
wordlist.

%prep
%setup -q
%autopatch -p1

%build
%make CFLAGS="-DOPENSSL"

%install
# make install is broken
install -D -pm 755 cowpatty %{buildroot}%{_bindir}/%{name}
install -D -pm 755 genpmk %{buildroot}%{_bindir}/genpmk

%files 
%doc AUTHORS COPYING README FAQ TODO CHANGELOG
%{_bindir}/*
