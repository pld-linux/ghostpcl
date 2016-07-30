# TODO:
#	- prevent linking pspcl6 and pcl6 with expat
#	- fix GS_LIB_DEFAULT path to gs_init.ps (pspcl6)
#	  how about GS_DOT_VERSION?

Summary:	PostScript, PDF and XPS interpreter and renderer
Summary(pl.UTF-8):	Interpreter i renderer PostScriptu, PDF oraz XPS
Name:		ghostpcl
Version:	1.54
Release:	9
License:	GPL v2
Group:		Applications/Graphics
#Source0:	http://mirror.cs.wisc.edu/pub/mirrors/ghost/GPL/ghostpdl/ghostpdl-%{version}.tar.bz2
#Source0:	http://www.ctan.org/get/support/ghostscript/GPL/ghostpdl/ghostpdl-%{version}.tar.bz2
Source0:	http://ghostscript.com/releases/ghostpdl-%{version}.tar.bz2
# Source0-md5:	228f96df51d192b95bc4d9340015aa9e
Patch0:		%{name}-fonts_locations.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-format-security.patch
URL:		http://www.artifex.com/downloads/
#BuildRequires:	XFree86-devel
BuildRequires:	expat-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	zlib-devel
Suggests:	fonts-TTF-urw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GhostPCL is Artifex Software's implementation of the PCL-5(TM) and
PCL-XL(TM) family of page description languages. For more information
please see the documentation included with the source package.

%description -l pl.UTF-8
GhostPCL jest implementacją języków z rodzin PCL-5(TM) i PCL-XL(TM)
opisujących stronę. Więcej informacji znajduje się w dokumentacji
załączonej do pakietu.

%prep
%setup -q -n ghostpdl-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	XCFLAGS="%{rpmcflags}" \
	XLDFLAGS="%{rpmldflags}" \
	SHARE_JPEG=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install language_switch/obj/pspcl6 main/obj/pcl6 tools/pcl2pdfwr xps/obj/gxps $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/ghostpdl.pdf
%attr(755,root,root) %{_bindir}/gxps
%attr(755,root,root) %{_bindir}/pcl2pdfwr
%attr(755,root,root) %{_bindir}/pcl6
%attr(755,root,root) %{_bindir}/pspcl6
