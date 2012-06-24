Summary:	ROBODoc - extract documentation from source code
Summary(pl):	ROBODoc - narz�dzie wyci�gaj�ce dokumentacj� z kodu �r�d�owego
Name:		robodoc
Version:	3.2.3
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/robodoc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ROBODoc is a documentation tool (based on the AutoDocs program written
a long time ago by Commodore). It extracts specially formated comment
headers from the source file and puts them in a separate file. ROBODoc
thus allows you to include the program documentation in the source
code and avoid having to maintain two separate documents.

ROBODoc can format the documentation in HTML, ASCII, AmigaGuide,
LaTeX, or RTF format. It is even possible to include parts of the
source code with function names that point their the documentation. It
also can create index tables for all your variables, classes,
functions, etc.

The best feature of ROBODoc is that it works with many languages:
Assembler, C, Perl, LISP, Occam, Tcl/Tk, Pascal, Fortran, shell
scripts, and COBOL, basically any language that supports
comments/remarks.

%description -l pl
ROBODoc to narz�dzie do dokumentacji (bazuj�ce na programie AutoDocs
napisanym dawno temu przez Commodore). Wyci�ga ono specjalnie
sformatowane nag��wki z komentarzami z plik�w �r�d�owych u umieszcza
je w osobnym pliku. ROBODoc pozwala na do��czanie dokumentacji
programu w kodzie �r�d�owym i zapobiega konieczno�ci zarz�dzania dwoma
oddzielnymi dokumentami.

ROBODoc mo�e formatowa� dokumentacj� w formatach: HTML, ASCII,
AmigaGuide, LaTeX oraz RTF. Mo�na tak�e do��cza� cz�ci kodu
�r�d�owego z nazwami funkcji wskazanymi w ich dokumentacji. Mo�e tak�e
tworzy� tabele z indeksami wszystkich zmiennych, klas, funkcji itp.

Najlepsz� cech� ROBODoc jest to, �e dzia�a z wieloma j�zykami:
asembler, C, Perl, LISP, Occam, Tcl/Tk, Pascal, Fortran, skrypty
pow�oki i COBOL; og�lnie z ka�dym j�zykiem obs�uguj�cy komentarze.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
#%{__automake}
%configure
#--prefix=$RPM_BUILD_ROOT%{_prefix} --mandir=$RPM_BUILD_ROOT%{_mandir}
%{__make}
#docdir=$RPM_BUILD_ROOT%{_prefix}/share/doc/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a Examples/* Headers $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Change* NEWS README TODO Docs/main.css Docs/robodoc.html
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man1/*
