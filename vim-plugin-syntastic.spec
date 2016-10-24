%define		plugin	syntastic
Summary:	Vim plugin: Automatic syntax checking
Name:		vim-plugin-%{plugin}
Version:	3.8.0
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/scrooloose/syntastic/archive/%{version}.tar.gz
# Source0-md5:	55500457c839ef704f15833c807cde3a
URL:		http://www.vim.org/scripts/script.php?script_id=2736
Requires:	vim-rt >= 4:7.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Syntastic is a syntax checking plugin that runs files through external
syntax checkers and displays any resulting errors to the user. This
can be done on demand, or automatically as files are saved. If syntax
errors are detected, the user is notified and is happy because they
didn't have to compile their code or execute their script to find
them.

%package doc
Summary:	Documentation for syntastic Vim plugin
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:7.4.2054-2

%description doc
Documentation for syntastic Vim plugin.

%prep
%setup -qn %{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/
cp -pr autoload doc plugin syntax_checkers $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%doc README.markdown CONTRIBUTING.md
%dir %{_vimdatadir}/autoload/syntastic
%{_vimdatadir}/autoload/syntastic/*.vim
%{_vimdatadir}/plugin/syntastic.vim
%dir %{_vimdatadir}/plugin/syntastic
%{_vimdatadir}/plugin/syntastic/*.vim
%{_vimdatadir}/syntax_checkers

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/syntastic.txt
%{_vimdatadir}/doc/syntastic-checkers.txt
