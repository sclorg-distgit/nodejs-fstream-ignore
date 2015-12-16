%{?scl:%scl_package nodejs-fstream-ignore}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-fstream-ignore
Version:    1.0.2
Release:    1%{?dist}
Summary:    A file stream object that can ignore files by globs
# a copy of the BSD license will be included in the next upstream release
# https://github.com/isaacs/fstream-ignore/commit/f5b9b1d981ff98ce1c92d4eac2b1aa91a142e421
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/fstream-ignore
Source0:    http://registry.npmjs.org/fstream-ignore/-/fstream-ignore-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/fstream-ignore
cp -pr ignore.js package.json %{buildroot}%{nodejs_sitelib}/fstream-ignore

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/fstream-ignore
%doc README.md example LICENSE

%changelog
* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-3
- New upstream release 1.0.2

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.7-2
- replace provides and requires with macro

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-1
- new upstream release 0.0.7

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-3
- restrict to compatible arches

* Wed May 22 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.6-3
- Add LICENSE file to the package

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-2
- add macro for EPEL6 dependency generation

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.6-2
- Add support for software collections
* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-1
- new upstream release 0.0.6

* Tue Jan 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-4
- fix License tag

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-3
- add missing build section
- write better summary

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-2
- clean up for submission

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-1
- initial package
