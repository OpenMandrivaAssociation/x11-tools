Name: x11-tools
Version: 1.0.0
Release: 15
Summary: X11 tools
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPL
BuildArch: noarch

# very useful tools
Requires: iceauth
Requires: lbxproxy
Requires: luit
Requires: setxkbmap
Requires: smproxy
Requires: xauth
Requires: xcmsdb
Requires: xconsole
Requires: xdpyinfo
Requires: xfindproxy
Requires: xfwp
Requires: xgamma
Requires: xhost
Requires: xinit
Requires: xkill
Requires: xmodmap
Requires: xrandr
Requires: xrdb
Requires: xset
Requires: xsetmode
Requires: xsetpointer
Requires: xsetroot
Requires: xstdcmap

# less useful tools
Requires: appres
Requires: editres
Requires: listres
Requires: rstart
Requires: x11-scripts
Requires: viewres
Requires: x11perf
Requires: xev
Requires: xcursorgen
Requires: xfsinfo
Requires: xlsatoms
Requires: xlsclients
Requires: xkbcomp
Requires: xkbevd
Requires: xkbprint
Requires: xkbutils
Requires: xprop
Requires: xrefresh
Requires: xtrap
Requires: xvidtune
Requires: xvinfo
Requires: xwininfo

# more tools
Requires: proxymngr
#Requires: xrx

# build tools
Requires: makedepend

%description
X11 tools

%files
%defattr(-,root,root)


%changelog
* Fri Apr 15 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.0.0-10mdv2011.0
+ Revision: 653197
- Do not requires xrx

* Fri Dec 10 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.0-9mdv2011.0
+ Revision: 620448
- Rebuild for 2011.0

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-8mdv2010.1
+ Revision: 524368
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.0-7mdv2009.1
+ Revision: 351249
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 226012
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2008.1
+ Revision: 179620
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdv2008.0
+ Revision: 75662
- rebuild


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 18 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-18 15:10:15 (27613)
- this is for sure noarch

* Thu May 18 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-18 13:55:29 (27608)
- adding packager tag\n-Fixed requires for x11-scripts

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

