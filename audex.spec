Summary:		Audio grabber tool for CD-ROM drives based on KDE 4
Name:		audex
Version:		0.74b1
Release:		2
License:		GPLv3
Group:		Sound
URL:		http://kde.maniatek.com/audex/
Source0:		http://kde.maniatek.com/audex/files/%{name}-%{version}.tar.bz2
Patch0:		audex-0.74b1-fix-lseek-not-declared.patch
Requires:	kdebase4-runtime
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	kdelibs4-devel 
BuildRequires:	phonon-devel
BuildRequires:	cdda-devel
BuildRequires:	automoc4
BuildRequires:	python-eyed3
BuildRequires:	libkcddb-devel >= 4.9
BuildRequires:	libkcompactdisc-devel >= 4.9

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
%doc CHANGELOG LICENCE README TODO
%{_kde_bindir}/%{name}
%{_kde_datadir}/applications/kde4/%{name}*.desktop
%{_kde_datadir}/apps/solid/actions/%{name}*.desktop
%{_kde_datadir}/apps/%{name}
# This is useless: already listed by %find_lang
#{_kde_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_kde_iconsdir}/hicolor/*/*/*.png

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
export CFLAGS="%{optflags} -fno-strict-aliasing" CXXFLAGS="%{optflags} -fno-strict-aliasing"
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html


%changelog
* Wed Oct 10 2012 Giovanni Mariani <mc2374@mclink.it> 0.74b1-1
- Removed Source1: from release 0.73 it is integrated in the source tarball
- Removed unused %%define
- Removed BuildRoot, defattr, %%clean section and %%mkrel
- Updated URL tag
- Made sure the Description text wraps at 76th char and corrected some typos
- Added some docs (it makes rpmlint happy)
- Replaced BReq for now-removed kdemultimedia4-devel with the actual needed
  devel packages (libkcddb and libkcompactdisk)
- Disable strict aliasing error to fix build
- Added P0 to unbroke the build another time

* Sun Jan 30 2011 Bruno Cornec <bcornec@mandriva.org> 0.74b1-1mdv2011.0
+ Revision: 634338
- Update audex to upstream 0.74b1

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Wed Oct 21 2009 Anne Nicolas <ennael@mandriva.org> 0.71b5-2mdv2010.0
+ Revision: 458547
- fix group

* Sat Jul 04 2009 Bruno Cornec <bcornec@mandriva.org> 0.71b5-1mdv2010.0
+ Revision: 392038
- Import audex 0.71b5
- create audex

