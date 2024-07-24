# Generated by rust2rpm 26
%bcond_without check

%global crate onefetch

Name:           rust-onefetch
Version:        2.21.0
Release:        %autorelease
Summary:        Command-line Git information tool

License:        MIT
URL:            https://crates.io/crates/onefetch
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          onefetch-fix-metadata-auto.diff

BuildRequires:  anda-srpm-macros cargo-rpm-macros >= 24
BuildRequires:  cmake

%global _description %{expand:
Command-line Git information tool.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
License:        (0BSD OR MIT OR Apache-2.0) AND Apache-2.0 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND BSD-3-Clause AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib AND (Zlib OR Apache-2.0 OR MIT)

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.md
%license resources/license.cache.zstd
%license src/info/license.rs
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/onefetch

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.md
%license %{crate_instdir}/resources/license.cache.zstd
%license %{crate_instdir}/src/info/license.rs
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fail-on-deprecated-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fail-on-deprecated-devel %{_description}

This package contains library source intended for building other packages which
use the "fail-on-deprecated" feature of the "%{crate}" crate.

%files       -n %{name}+fail-on-deprecated-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep_online

%build
cat<<EOF > license.sh
%{cargo_license} > LICENSE.dependencies
EOF
sed -i "s/--offline//g" license.sh
bash license.sh

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog