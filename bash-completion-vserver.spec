# TODO
# - add (v)poldek support
Summary:	bash-completion for vserver command
Name:		bash-completion-vserver
Version:	0.4.1
Release:	0.1
License:	GPL
Group:		Applications/Shells
Source0:	%{name}.sh
# Source0-md5:	20d9b2d8c50fe0ca9bb381d16daf2d7d
URL:		http://linux-vserver.org/util-vserver:Bash_Completion
Requires:	bash-completion
Requires:	util-vserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/bash_completion.d

%description
bash-completion for vserver command.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/vserver

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/*
