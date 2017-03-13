%{?scl:%scl_package nodejs-fstream-ignore}
%{!?scl:%global pkg_name %{name}}
%global enable_tests 0
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-fstream-ignore
Version:    1.0.5
Release:    1%{?dist}
Summary:    A file stream object that can ignore files by globs
# a copy of the BSD license will be included in the next upstream release
# https://github.com/isaacs/fstream-ignore/commit/f5b9b1d981ff98ce1c92d4eac2b1aa91a142e421
License:    ISC
URL:        https://github.com/isaacs/fstream-ignore
Source0:    http://registry.npmjs.org/fstream-ignore/-/fstream-ignore-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{enable_tests}
BuildRequires:    %{?scl_prefix}npm(mkdirp)
BuildRequires:    %{?scl_prefix}npm(rimraf)
BuildRequires:    %{?scl_prefix}npm(tap)
%endif

%description
%{summary}.

%prep
%setup -q -n package

#%nodejs_fixdep minimatch '>= 3.0.0'

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/fstream-ignore
cp -pr ignore.js package.json %{buildroot}%{nodejs_sitelib}/fstream-ignore

%nodejs_symlink_deps

%if 0%{enable_tests}
%check
%nodejs_symlink_deps --check
tap test/*.js --cov
%endif

%files
%{nodejs_sitelib}/fstream-ignore
%doc README.md LICENSE

%changelog
* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.5-1
- Updated with script
- source tarball no longer has tests and examples

* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-4
- Resolves: rhbz#1334856
- ^fixes wrong license

* Tue Feb 16 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-3
- Fix dependency version of minimatch

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
