Summary:	Audio grabber tool for CD-ROM drives based on KDE 4
Name:		audex
Version:	25.08.3
Release:	1
License:	GPLv3
Group:		Sound
URL:		https://invent.kde.org/multimedia/audex
Source0:	https://download.kde.org/stable/release-service/%{version}/src/audex-%{version}.tar.xz
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(KCddb6)
BuildRequires:	cmake(KF6ColorScheme)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	pkgconfig(libcdio_cdda)
BuildRequires:	pkgconfig(libcdio_paranoia)

%description
Audex is a new audio grabber tool for CD-ROM drives based on KDE 4.
It creates profiles for LAME, OGG Vorbis (oggenc), FLAC, FAAC
(MP4/M4A/AAC) and RIFF WAVE: please install your favorite encoder. Of
course for WAVE no external encoder is needed! Beyond you can define
custom profile, which means that audex works together with command line
encoders in general.
Some features are:
* Extracting with CDDA Paranoia. So you have quite perfect audio quality.
* Extracting and encoding run parallel.
* Filename editing with local and remote CDDB/FreeDB database.
* Metadata correction tools like capitalize etc.
* Multi-profile extraction (with one command-line encoder per profile).
* Fetch covers from the Internet and store them in the database.
* Create play-lists, cover and template-based-info files in target
  directory.
* Creates extraction and encoding protocols.
* Transfer files with KDE KIO-Slaves.

%files -f %{name}.lang
%{_bindir}/audex
%{_datadir}/applications/org.kde.audex.desktop
%{_datadir}/audex
%{_datadir}/icons/hicolor/scalable/apps/org.kde.audex.svg
%{_datadir}/metainfo/org.kde.audex.appdata.xml
%{_datadir}/solid/actions/audex-rip-audiocd.desktop
