# TODO:
#	- prevent linking pspcl6 and pcl6 with expat
#	- fix GS_LIB_DEFAULT path to gs_init.ps (pspcl6)
#	  how about GS_DOT_VERSION?
#	- rename urwfonts subpackage to font-TTF-urw
#	- create alternate Type1 font subpackage:
#	  http://mirror.cs.wisc.edu/pub/mirrors/ghost/AFPL/GhostPCL/urwfonts_t1-1.40.tar.bz2

%define	urwfonts_ver	1.41

Summary:	PostScript, PDF and XPS interpreter and renderer
Summary(pl.UTF-8):	Interpreter i renderer PostScriptu, PDF oraz XPS
Name:		ghostpcl
Version:	1.54
Release:	6
License:	GPL v2
Group:		Applications/Graphics
#Source0:	http://mirror.cs.wisc.edu/pub/mirrors/ghost/GPL/ghostpdl/ghostpdl-%{version}.tar.bz2
#Source0:	http://www.ctan.org/get/support/ghostscript/GPL/ghostpdl/ghostpdl-%{version}.tar.bz2
Source0:	http://ghostscript.com/releases/ghostpdl-%{version}.tar.bz2
# Source0-md5:	228f96df51d192b95bc4d9340015aa9e
#Source1:	http://mirror.cs.wisc.edu/pub/mirrors/ghost/AFPL/GhostPCL/urwfonts-%{urwfonts_ver}.tar.bz2
Source1:	http://www.ctan.org/get/nonfree/support/ghostscript/AFPL/GhostPCL/urwfonts-%{urwfonts_ver}.tar.bz2
# Source1-md5:	6d65230fa5e9783a0b5942b55dc5219f
Patch0:		%{name}-fonts_locations.patch
Patch1:		%{name}-make.patch
URL:		http://www.artifex.com/downloads/
#BuildRequires:	XFree86-devel
BuildRequires:	expat-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
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
License:	Alladin Free Public License
Group:		Fonts
Requires(post,postun):	fontpostinst

%description urwfonts
URW fonts in TTF format for GhostPCL.

%description urwfonts -l pl.UTF-8
Fonty URW w formacie TTF dla GhostPCL-a.

%prep
%setup -q -n ghostpdl-%{version} -a1
%patch0 -p1
%patch1 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	XCFLAGS="%{rpmcflags}" \
	XLDFLAGS="%{rpmldflags}" \
	SHARE_JPEG=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/fonts/TTF}
install language_switch/obj/pspcl6 main/obj/pcl6 tools/pcl2pdfwr xps/obj/gxps $RPM_BUILD_ROOT%{_bindir}
install urwfonts*/*.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF

%clean
rm -rf $RPM_BUILD_ROOT

%post urwfonts
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/*

%files urwfonts
%defattr(644,root,root,755)
%{_datadir}/fonts/TTF
