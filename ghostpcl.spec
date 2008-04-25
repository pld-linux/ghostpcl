
%define	urwfonts_ver	1.41

Summary:	PostScript & PDF interpreter and renderer
Summary(pl.UTF-8):	Interpreter i renderer PostScriptu i PDF
Name:		ghostpcl
Version:	1.52
Release:	1
License:	GPL
Group:		Applications/Graphics
#Source0:	http://mirror.cs.wisc.edu/pub/mirrors/ghost/GPL/ghostpdl/ghostpdl-%{version}.tar.bz2
#Source0:	http://www.ctan.org/get/support/ghostscript/GPL/ghostpdl/ghostpdl-%{version}.tar.bz2
Source0:	http://ghostscript.com/releases/ghostpdl-%{version}.tar.bz2
# Source0-md5:	7bc095bd6fd67e52a758608accb23bef
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
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
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
	XCFLAGS="%{rpmcflags}" \
	XLDFLAGS="--as-needed" \
	SHARE_JPEG=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/fonts/TTF}
install language_switch/obj/pspcl6 main/obj/pcl6 xps/obj/gxps $RPM_BUILD_ROOT%{_bindir}
install urwfonts*/*.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/TTF

%clean
rm -rf $RPM_BUILD_ROOT

%post urwfonts
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/pcl*

%files urwfonts
%defattr(644,root,root,755)
%{_datadir}/fonts/TTF
