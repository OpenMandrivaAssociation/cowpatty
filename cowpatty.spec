%define name cowpatty
%define version 4.3
%define release %mkrel 2

Name: %{name}
Summary: Brute-force dictionary attack against WPA-PSK
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tgz
Group: Networking/Other
URL: http://cowpatty.sf.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: openssl-devel libpcap-devel
License: GPLv2

%description
coWPAtty is designed to audit the pre-shared key (PSK) selection for WPA
networks based on the TKIP protocol. Supply a libpcap file that includes the
TKIP four-way handshake to mount an offline dictionary attack with a supplied
wordlist.

See the README for more details.

%prep
%setup -q 

%build
make
make love

%install
rm -rf $RPM_BUILD_ROOT 
# make install is broken
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp cowpatty genpmk $RPM_BUILD_ROOT/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING FAQ README TODO dict 
%{_bindir}/*
