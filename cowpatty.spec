%define name cowpatty
%define version 2.0
%define release %mkrel 6

Name: %{name}
Summary: Brute-force dictionary attack against WPA-PSK
Version: %{version}
Release: %{release}
Source: Cowpatty-%{version}.tar.bz2
Group: Networking/Other
URL: http://new.remote-exploit.org/index.php/Codes_main
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: openssl-devel libpcap-devel
License: GPL

%description
coWPAtty is designed to audit the pre-shared key (PSK) selection for WPA
networks based on the TKIP protocol. Supply a libpcap file that includes the
TKIP four-way handshake to mount an offline dictionary attack with a supplied
wordlist.

See the README for more details.

%prep
%setup -q -n %name

%build
make
make love

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp cowpatty $RPM_BUILD_ROOT/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING FAQ README TODO WISHLIST dict
%{_bindir}/*


