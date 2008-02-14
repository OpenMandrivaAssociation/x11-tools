Name: x11-tools
Version: 1.0.0
Release: %mkrel 4
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
Requires: xrx

# build tools
Requires: makedepend

%description
X11 tools

%files
%defattr(-,root,root)
