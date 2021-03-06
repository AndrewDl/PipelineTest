%define         majorminor      0.10
%define		gstreamer	gstreamer010

Name: 		%{gstreamer}
Version: 	0.10.0
Release: 	1
Summary: 	GStreamer streaming media framework runtime

Group: 		Applications/Multimedia
License: 	LGPL
URL:		http://gstreamer.freedesktop.org/
Vendor:         GStreamer Backpackers Team <package@gstreamer.freedesktop.org>
Source: 	http://gstreamer.freedesktop.org/src/gstreamer/gstreamer-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define 	_glib2		@GLIB2_REQ@
%define 	_libxml2	2.4.9

Requires: 	glib2 >= %_glib2
Requires: 	libxml2 >= %_libxml2
Requires:	popt > 1.6

# Provides:	gstreamer =%{version}-%{release}

BuildRequires: 	glib2-devel >= %_glib2
BuildRequires: 	libxml2-devel >= %_libxml2
BuildRequires: 	bison
BuildRequires: 	flex
BuildRequires: 	m4
BuildRequires: 	check
BuildRequires: 	gtk-doc >= 1.1
BuildRequires: 	gcc
BuildRequires: 	gettext
BuildRequires: 	zlib-devel
BuildRequires:  popt > 1.6
Requires(pre):	/sbin/ldconfig
Requires(post):	/sbin/ldconfig

### documentation requirements
BuildRequires:  python2
BuildRequires:  openjade
BuildRequires:  jadetex
BuildRequires:  libxslt
BuildRequires:  docbook-style-dsssl
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:	transfig
BuildRequires:  xfig
BuildRequires:  netpbm-progs
BuildRequires:  ghostscript

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new 
plugins.

%package devel
Summary: 	Libraries/include files for GStreamer streaming media framework
Group: 		Development/Libraries

Requires: 	%{name} = %{version}-%{release}
Requires: 	glib2-devel >= %_glib2
Requires: 	libxml2-devel >= %_libxml2

%description devel
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains the libraries and includes files necessary to develop
applications and plugins for GStreamer.

%package -n %{gstreamer}-tools
Summary: 	tools for GStreamer streaming media framework
Group: 		Applications/Multimedia

%description -n %{gstreamer}-tools
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new   
plugins.

This package contains wrapper scripts for the command-line tools that work
with different major/minor versions of GStreamer.
                                                                                
%prep
%setup -q -n gstreamer-%{version}

%build
%configure \
  --with-cachedir=%{_localstatedir}/cache/gstreamer-%{majorminor} \
  --enable-gtk-doc --enable-docbook \
  --disable-tests --disable-examples
                                                                                
make

%install  
rm -rf $RPM_BUILD_ROOT

# Install doc temporarily in order to be included later by rpm
%makeinstall docdir="`pwd`/installed-doc"

%find_lang gstreamer-%{majorminor}
# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Create empty cache directory
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/cache/gstreamer-%{majorminor}
                                                                                
%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f gstreamer-%{majorminor}.lang
%defattr(-, root, root, -)
# %doc AUTHORS COPYING ABOUT-NLS README RELEASE MAINTAINERS ChangeLog CHANGES-0.9 DOCBUILDING INSTALL
%{_libdir}/libgstreamer-%{majorminor}.so.*
%{_libdir}/libgstbase-%{majorminor}.so.*
%{_libdir}/libgstcontroller-%{majorminor}.so.*
%{_libdir}/libgstdataprotocol-%{majorminor}.so.*
%{_libdir}/libgstnet-%{majorminor}.so.*

%dir %{_libdir}/gstreamer-%{majorminor}
%{_libdir}/gstreamer-%{majorminor}/libgstcoreelements.so
%{_libdir}/gstreamer-%{majorminor}/libgstcoreindexers.so

%{_bindir}/gst-feedback-%{majorminor}
%{_bindir}/gst-inspect-%{majorminor}
%{_bindir}/gst-launch-%{majorminor}
%{_bindir}/gst-md5sum-%{majorminor}
%{_bindir}/gst-typefind-%{majorminor}
%{_bindir}/gst-xmlinspect-%{majorminor}
%{_bindir}/gst-xmllaunch-%{majorminor}
%{_mandir}/man1/gst-feedback-%{majorminor}.*
%{_mandir}/man1/gst-inspect-%{majorminor}.*
%{_mandir}/man1/gst-launch-%{majorminor}.*
%{_mandir}/man1/gst-md5sum-%{majorminor}.*
%{_mandir}/man1/gst-typefind-%{majorminor}.*
%{_mandir}/man1/gst-xmlinspect-%{majorminor}.*
%{_mandir}/man1/gst-xmllaunch-%{majorminor}.*

%dir %{_localstatedir}/cache/gstreamer-%{majorminor}

%files -n %{gstreamer}-tools
%defattr(-, root, root, -)
%{_bindir}/gst-feedback
%{_bindir}/gst-inspect
%{_bindir}/gst-launch
%{_bindir}/gst-md5sum
%{_bindir}/gst-typefind
%{_bindir}/gst-xmlinspect
%{_bindir}/gst-xmllaunch

%files devel
%defattr(-, root, root, -)
%doc installed-doc/faq installed-doc/pwg installed-doc/manual
%dir %{_includedir}/gstreamer-%{majorminor}
%dir %{_includedir}/gstreamer-%{majorminor}/gst
%{_includedir}/gstreamer-%{majorminor}/gst/*.h
%{_includedir}/gstreamer-%{majorminor}/gst/controller/gstcontroller.h
%{_includedir}/gstreamer-%{majorminor}/gst/net/gstnet.h
%{_includedir}/gstreamer-%{majorminor}/gst/net/gstnetclientclock.h
%{_includedir}/gstreamer-%{majorminor}/gst/net/gstnettimepacket.h
%{_includedir}/gstreamer-%{majorminor}/gst/net/gstnettimeprovider.h
%{_includedir}/gstreamer-%{majorminor}/gst/base
%{_includedir}/gstreamer-%{majorminor}/gst/dataprotocol

%{_libdir}/libgstreamer-%{majorminor}.so
%{_libdir}/libgstdataprotocol-%{majorminor}.so
%{_libdir}/libgstbase-%{majorminor}.so
%{_libdir}/libgstcontroller-%{majorminor}.so
%{_libdir}/libgstnet-%{majorminor}.so


%{_datadir}/aclocal/gst-element-check-%{majorminor}.m4
%{_libdir}/pkgconfig/gstreamer-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-base-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-dataprotocol-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-controller-%{majorminor}.pc
%{_libdir}/pkgconfig/gstreamer-net-%{majorminor}.pc

%doc %{_datadir}/gtk-doc/html/gstreamer-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gstreamer-libs-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gstreamer-plugins-%{majorminor}
                                                                                
%changelog
* Fri Sep 02 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- clean up a little

* Thu Jun 09 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- clean up spec for 0.9 builds

* Thu Feb 12 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- sync with 0.7.4 fedora spec

* Thu Feb 05 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- bump gtk-doc required version to 1.0 for the new options used

* Wed Feb 04 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- add -common package containing frontend wrapper binaries

* Mon Dec 01 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- changed documentation buildrequires

* Sun Nov 09 2003 Christian Schaller <Uraeus@gnome.org>
- Fix spec to handle new bytestream library 

* Sun Aug 17 2003 Christian Schaller <uraeus@gnome.org>
- Remove docs build from RPM as the build is broken
- Fix stuff since more files are versioned now
- Remove wingo schedulers
- Remove putbits stuff

* Sun May 18 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- devhelp files are now generated by gtk-doc, changed accordingly

* Sun Mar 16 2003 Christian F.K. Schaller <Uraeus@gnome.org>
- Add gthread scheduler

* Sat Dec 07 2002 Thomas Vander Stichele <thomas at apestaart dot org>
- define majorminor and use it everywhere
- full parallel installability

* Tue Nov 05 2002 Christian Schaller <Uraeus@linuxrising.org>
- Add optwingo scheduler
* Sat Oct 12 2002 Christian Schaller <Uraeus@linuxrising.org>
- Updated to work better with default RH8 rpm
- Added missing unspeced files
- Removed .a and .la files from buildroot

* Sat Sep 21 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added gst-md5sum

* Tue Sep 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- adding flex to buildrequires

* Fri Sep 13 2002 Christian F.K. Schaller <Uraeus@linuxrising.org>
- Fixed the schedulers after the renaming
* Sun Sep 08 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added transfig to the BuildRequires:

* Sat Jun 22 2002 Thomas Vander Stichele <thomas@apestaart.org>
- moved header location

* Mon Jun 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added popt
- removed .la

* Fri Jun 07 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added release of gstreamer to req of gstreamer-devel
- changed location of API docs to be in gtk-doc like other gtk-doc stuff
- reordered SPEC file

* Mon Apr 29 2002 Thomas Vander Stichele <thomas@apestaart.org>
- moved html docs to gtk-doc standard directory

* Tue Mar 5 2002 Thomas Vander Stichele <thomas@apestaart.org>
- move version defines of glib2 and libxml2 to configure.ac
- add BuildRequires for these two libs

* Sun Mar 3 2002 Thomas Vander Stichele <thomas@apestaart.org>
- put html docs in canonical place, avoiding %doc erasure
- added devhelp support, current install of it is hackish

* Sat Mar 2 2002 Christian Schaller <Uraeus@linuxrising.org>
- Added documentation to build

* Mon Feb 11 2002 Thomas Vander Stichele <thomas@apestaart.org>
- added libgstbasicscheduler
- renamed libgst to libgstreamer

* Fri Jan 04 2002 Christian Schaller <Uraeus@linuxrising.org>
- Added configdir parameter as it seems the configdir gets weird otherwise

* Thu Jan 03 2002 Thomas Vander Stichele <thomas@apestaart.org>
- split off gstreamer-editor from core
- removed gstreamer-gnome-apps

* Sat Dec 29 2001 Rodney Dawes <dobey@free.fr>
- Cleaned up the spec file for the gstreamer core/plug-ins split
- Improve spec file

* Sat Dec 15 2001 Christian Schaller <Uraeus@linuxrising.org>
- Split of more plugins from the core and put them into their own modules
- Includes colorspace, xfree and wav
- Improved package Require lines
- Added mp3encode (lame based) to the SPEC

* Wed Dec 12 2001 Christian Schaller <Uraeus@linuxrising.org>
- Thomas merged mpeg plugins into one
* Sat Dec 08 2001 Christian Schaller <Uraeus@linuxrising.org>
- More minor cleanups including some fixed descriptions from Andrew Mitchell

* Fri Dec 07 2001 Christian Schaller <Uraeus@linuxrising.org>
- Added logging to the make statement

* Wed Dec 05 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated in preparation for 0.3.0 release

* Fri Jun 29 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated for 0.2.1 release
- Split out the GUI packages into their own RPM
- added new plugins (FLAC, festival, quicktime etc.)

* Sat Jun 09 2001 Christian Schaller <Uraeus@linuxrising.org>
- Visualisation plugins bundled out togheter
- Moved files sections up close to their respective descriptions

* Sat Jun 02 2001 Christian Schaller <Uraeus@linuxrising.org>
- Split the package into separate RPMS, 
  putting most plugins out by themselves.

* Fri Jun 01 2001 Christian Schaller <Uraeus@linuxrising.org>
- Updated with change suggestions from Dennis Bjorklund

* Tue Jan 09 2001 Erik Walthinsen <omega@cse.ogi.edu>
- updated to build -devel package as well

* Sun Jan 30 2000 Erik Walthinsen <omega@cse.ogi.edu>
- first draft of spec file

