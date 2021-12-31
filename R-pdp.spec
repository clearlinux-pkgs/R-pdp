#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pdp
Version  : 0.7.0
Release  : 32
URL      : https://cran.r-project.org/src/contrib/pdp_0.7.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pdp_0.7.0.tar.gz
Summary  : Partial Dependence Plots
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-pdp-lib = %{version}-%{release}
Requires: R-ggplot2
Requires: R-gridExtra
Requires: R-magrittr
Requires: R-plyr
Requires: R-viridis
BuildRequires : R-ggplot2
BuildRequires : R-gridExtra
BuildRequires : R-magrittr
BuildRequires : R-plyr
BuildRequires : R-viridis
BuildRequires : buildreq-R

%description
A general framework for constructing partial dependence (i.e., marginal effect)
plots from various types machine learning models in R.

%package lib
Summary: lib components for the R-pdp package.
Group: Libraries

%description lib
lib components for the R-pdp package.


%prep
%setup -q -c -n pdp
cd %{_builddir}/pdp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589785661

%install
export SOURCE_DATE_EPOCH=1589785661
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pdp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pdp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pdp
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pdp || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pdp/CITATION
/usr/lib64/R/library/pdp/DESCRIPTION
/usr/lib64/R/library/pdp/INDEX
/usr/lib64/R/library/pdp/Meta/Rd.rds
/usr/lib64/R/library/pdp/Meta/data.rds
/usr/lib64/R/library/pdp/Meta/features.rds
/usr/lib64/R/library/pdp/Meta/hsearch.rds
/usr/lib64/R/library/pdp/Meta/links.rds
/usr/lib64/R/library/pdp/Meta/nsInfo.rds
/usr/lib64/R/library/pdp/Meta/package.rds
/usr/lib64/R/library/pdp/NAMESPACE
/usr/lib64/R/library/pdp/NEWS.md
/usr/lib64/R/library/pdp/R/pdp
/usr/lib64/R/library/pdp/R/pdp.rdb
/usr/lib64/R/library/pdp/R/pdp.rdx
/usr/lib64/R/library/pdp/data/Rdata.rdb
/usr/lib64/R/library/pdp/data/Rdata.rds
/usr/lib64/R/library/pdp/data/Rdata.rdx
/usr/lib64/R/library/pdp/help/AnIndex
/usr/lib64/R/library/pdp/help/aliases.rds
/usr/lib64/R/library/pdp/help/figures/README-example-rf-1.png
/usr/lib64/R/library/pdp/help/figures/README-example-rf-2-1.png
/usr/lib64/R/library/pdp/help/figures/README-example-rf-3-1.png
/usr/lib64/R/library/pdp/help/figures/README-example-svm-1.png
/usr/lib64/R/library/pdp/help/figures/README-example-svm-2-1.png
/usr/lib64/R/library/pdp/help/figures/pdp-logo.png
/usr/lib64/R/library/pdp/help/figures/pdp-logo.svg
/usr/lib64/R/library/pdp/help/figures/pdp-logos.png
/usr/lib64/R/library/pdp/help/paths.rds
/usr/lib64/R/library/pdp/help/pdp.rdb
/usr/lib64/R/library/pdp/help/pdp.rdx
/usr/lib64/R/library/pdp/html/00Index.html
/usr/lib64/R/library/pdp/html/R.css
/usr/lib64/R/library/pdp/tests/testthat.R
/usr/lib64/R/library/pdp/tests/testthat/test-partial.R
/usr/lib64/R/library/pdp/tests/testthat/test-utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pdp/libs/pdp.so
