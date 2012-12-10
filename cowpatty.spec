%define name cowpatty
%define version 4.3
%define release %mkrel 3

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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 4.3-3mdv2011.0
+ Revision: 610165
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 4.3-2mdv2010.1
+ Revision: 537464
- rebuild

* Sat Jan 16 2010 Michael Scherer <misc@mandriva.org> 4.3-1mdv2010.1
+ Revision: 492194
- update to latest release
- new url
- correct License tag

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 2.0-7mdv2010.0
+ Revision: 437129
- rebuild

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0-6mdv2009.1
+ Revision: 298236
- rebuilt against libpcap-1.0.0

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.0-5mdv2009.0
+ Revision: 243691
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0-3mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Feb 19 2007 Pascal Terjan <pterjan@mandriva.org> 2.0-3mdv2007.0
+ Revision: 122907
- rebuild
- Import cowpatty

* Fri Mar 17 2006 Pascal Terjan <pterjan@mandriva.org> 2.0-2mdk
- rebuild for new libcrypto
- mkrel

* Thu Aug 11 2005 Pascal Terjan <pterjan@mandriva.org> 2.0-1mdk
- First Mandriva release

