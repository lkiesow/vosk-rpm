%global srcname webvtt-py

Name:           python-%{srcname}
Version:        0.4.6
Release:        1%{?dist}
Summary:        Read, write and segment WebVTT caption files in Python.

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/glut23/webvtt-py/archive/refs/tags/0.4.6.tar.gz

BuildArch:      noarch

%global _description %{expand:
webvtt-py is a Python module for reading/writing WebVTT caption files.
It also features caption segmentation useful when captioning HLS videos.
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/webvtt_py-*.egg-info
%{python3_sitelib}/webvtt/
%{_bindir}/webvtt

%changelog
* Sat Jun 26 2021 Lars Kiesow <lkiesow@uos.de> - 0.4.6-1
- Initial build
