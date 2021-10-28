#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tomli
Version  : 1.2.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/ec/38/8eccdc662c61aed187d5f5b168c18b1d2de3827976c3691e4da8be7375aa/tomli-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ec/38/8eccdc662c61aed187d5f5b168c18b1d2de3827976c3691e4da8be7375aa/tomli-1.2.0.tar.gz
Summary  : A lil' TOML parser
Group    : Development/Tools
License  : MIT
Requires: tomli-license = %{version}-%{release}
Requires: tomli-python = %{version}-%{release}
Requires: tomli-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
[![Build Status](https://github.com/hukkin/tomli/workflows/Tests/badge.svg?branch=master)](https://github.com/hukkin/tomli/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)
[![codecov.io](https://codecov.io/gh/hukkin/tomli/branch/master/graph/badge.svg)](https://codecov.io/gh/hukkin/tomli)
[![PyPI version](https://img.shields.io/pypi/v/tomli)](https://pypi.org/project/tomli)

%package license
Summary: license components for the tomli package.
Group: Default

%description license
license components for the tomli package.


%package python
Summary: python components for the tomli package.
Group: Default
Requires: tomli-python3 = %{version}-%{release}

%description python
python components for the tomli package.


%package python3
Summary: python3 components for the tomli package.
Group: Default
Requires: python3-core
Provides: pypi(tomli)

%description python3
python3 components for the tomli package.


%prep
%setup -q -n tomli-1.2.0
cd %{_builddir}/tomli-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627658166
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tomli
cp %{_builddir}/tomli-1.2.0/LICENSE %{buildroot}/usr/share/package-licenses/tomli/9da6ca26337a886fb3e8d30efd4aeda623dc9ade
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tomli/9da6ca26337a886fb3e8d30efd4aeda623dc9ade

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
