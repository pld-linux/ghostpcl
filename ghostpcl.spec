Summary:	PostScript & PDF interpreter and renderer
Summary(pl.UTF-8):	Interpreter i renderer PostScriptu i PDF
Name:		ghostpcl
Version:	1.38p1
Release:	1
License:	Alladin Free Public License (see Public.htm)
Group:		Applications/Graphics
#Source0Download: http://www.artifex.com/downloads/
Source0:	ftp://mirror.cs.wisc.edu/pub/mirrors/ghost/AFPL/GhostPCL/%{name}_%{version}.tar.gz
# Source0-md5:	5067678a6b3b682423f74c92b5c82013
Patch0:		%{name}-fonts_locations.patch
Patch1:		%{name}-make.patch
URL:		http://www.artifex.com/downloads/
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GhostPCL is Artifex Software's implementation of the PCL-5(TM) and
PCL-XL(TM) family of page description languages. For more information
please see the documentation included with the source package.

%description -l pl.UTF-8
GhostPCL jest implementacją języków z rodzin PCL-5(TM) i PCL-XL(TM)
opisujących stronę. Więcej informacji znajduje się w dokumentacji
załączonej do pakietu.

%package urwfonts
Summary:	URW fonts in TTF format for GhostPCL
Summary(pl.UTF-8):	Fonty URW w formacie TTF dla GhostPCL-a
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description urwfonts
URW fonts in TTF format for GhostPCL.

%description urwfonts -l pl.UTF-8
Fonty URW w formacie TTF dla GhostPCL-a.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} pcl6 \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install main/obj/pcl6 $RPM_BUILD_ROOT%{_bindir}
install urwfonts/*.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README doc/*
%attr(755,root,root) %{_bindir}/pcl*

%files urwfonts
%defattr(644,root,root,755)
%{_datadir}/%{name}
