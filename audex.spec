%define iconname %{name}.png

Summary:	Audio grabber tool for CD-ROM drives based on KDE 4
Name:		audex
Version:	0.71b5
Release:	%mkrel 1
License:	GPLv3
Group:		Databases
URL:		http://opensource.maniatek.de/audex/
Source0:		http://opensource.maniatek.de/audex/files/%{name}-%{version}.tar.bz2
Source1:		fr.po
Requires:	kdebase4-runtime
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	kdelibs4-devel 
BuildRequires:	phonon-devel
BuildRequires:	libcdda-devel
BuildRequires:	automoc4
BuildRequires:	kdemultimedia4-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
audex is a new audio grabber tool for CD-ROM drives based on KDE 4.

Audex creates profiles for LAME, OGG Vorbis (oggenc), FLAC, FAAC (MP4/M4A/AAC) and RIFF WAVE. Please install your favorite encoder.
Of course for WAVE no external encoder is needed!
Beyond you can define custom profile, which means, that audex works together with commmand line encoders in general.

Some features are:
* Extracting with CDDA Paranoia. So you have quite perfect audio quality.
* Extracting and encoding run parallel.
* Filename editing with local and remote CDDB/FreeDB database.
* Metadata correction tools like capitalize etc.
* Multi-profile extraction (with one commandline-encoder per profile).
* Fetch covers from the internet and store them in the database.
* Create playlists, cover and template-based-info files in target directory.
* Creates extraction and encoding protocols.
* Transfer files with KDE KIO-Slaves.

%files -f %{name}.lang
%defattr (-,root,root)
%{_kde_bindir}/%{name}
%{_kde_datadir}/applications/kde4/%{name}*.desktop
%{_kde_datadir}/apps/solid/actions/%{name}*.desktop
%{_kde_datadir}/apps/%{name}
%{_kde_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_kde_iconsdir}/hicolor/*/*/*.png

#--------------------------------------------------------------------

%prep
%setup -q -n %name
%{__cp} %{SOURCE1} po

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%find_lang %{name} --with-html

%clean 
rm -rf %{buildroot}
