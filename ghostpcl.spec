#

Summary:	PostScript & PDF interpreter and renderer
Summary(pl):	Bezp³atny interpreter i renderer PostScriptu i PDF
Name:		ghostpcl
Version:	1.38p1
Release:	0
License:	Alladin Free Public License
# http://www.artifex.com/downloads/doc/Public.htm
Group:		Applications/Graphics
Source0:	ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/AFPL/GhostPCL/%{name}_%{version}.tar.gz
# Source0-md5:	5067678a6b3b682423f74c92b5c82013
Source1:	http://www.artifex.com/downloads/doc/Public.htm
# Source1-md5:	fe9810925b8ea577727166a73b4d4f5c
#Source2:	http://www.artifex.com/downloads/doc/index.html     
# Source2-md5:	f810e4e35fce2c371ce9583972fad74b
#Source3:	http://www.artifex.com/downloads/doc/pclfaq.htm
# Source3-md5:	016b26e3a6b18186ce81063755f73e32
Patch0:		%{name}-fonts_locations.patch
URL:		http://www.artifex.com/downloads/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GhostPCL is Artifex Software's implementation of the PCL-5^tm and
PCL-XL^tm family of page description languages. For more information
please see the documentation included with the source package.

%description -l pl
GhostPCL jest implementacj± rodzin standardów PCL-5[tm] i PCL-XL[tm]
opisuj±cych 'stronê'. Wiêcej informacji znajdziesz w ¶rodku pakietu.

%package urwfonts
Summary:	GhostscriptPCL URWFonts
Summary(pl):	GhostscriptPCL czcionki URW
Group:		Applications/Graphics
#Requires:	%{name} = %{version}

%description urwfonts
TTF Fonts for ghostpcl. 

%description urwfonts -l pl
Czcionki TTF dla ghostpcl

%prep
%setup -q -n %{name}_%{version}

%build

#%{__make} fonts
%{__make} pcl6


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},\
%{_defaultdocdir}/%{name}-%{version}}

install main/obj/pcl6 $RPM_BUILD_ROOT%{_bindir}
install urwfonts/*.ttf $RPM_BUILD_ROOT%{_libdir}/%{name}/
install %{SOURCE1} $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}
#install %{SOURCE2} %{SOURCE3} $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}
install NEWS README doc/* $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_defaultdocdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/pcl*
#%{_mandir}/man*/*

%files urwfonts
%defattr(644,root,root,755)
%attr(755,root,root) 
%{_libdir}/%{name}
