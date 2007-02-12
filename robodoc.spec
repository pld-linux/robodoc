Summary:	ROBODoc - extract documentation from source code
Summary(pl.UTF-8):   ROBODoc - narzędzie wyciągające dokumentację z kodu źródłowego
Name:		robodoc
Version:	4.99.6
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f3cd237382d805130b817b3c8cd32834
URL:		http://robodoc.sourceforge.net/
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

%description -l pl.UTF-8
ROBODoc to narzędzie do dokumentacji (bazujące na programie AutoDocs
napisanym dawno temu przez Commodore). Wyciąga ono specjalnie
sformatowane nagłówki z komentarzami z plików źródłowych i umieszcza
je w osobnym pliku. ROBODoc pozwala na dołączanie dokumentacji
programu w kodzie źródłowym i zapobiega konieczności zarządzania dwoma
oddzielnymi dokumentami.

ROBODoc może formatować dokumentację w formatach: HTML, ASCII,
AmigaGuide, LaTeX oraz RTF. Można także dołączać części kodu
źródłowego z nazwami funkcji wskazanymi w ich dokumentacji. Może także
tworzyć tabele z indeksami wszystkich zmiennych, klas, funkcji itp.

Najlepszą cechą ROBODoc jest to, że działa z wieloma językami:
asembler, C, Perl, LISP, Occam, Tcl/Tk, Pascal, Fortran, skrypty
powłoki i COBOL; ogólnie z każdym językiem obsługujący komentarze.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
#%%{__automake}
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
%doc AUTHORS ChangeLog README TODO Docs/manual.xml
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man*/*
