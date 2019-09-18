#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jboss-logging
Version  : 3.1.0.cr2
Release  : 4
URL      : http://repo1.maven.org/maven2/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2-sources.jar
Source0  : http://repo1.maven.org/maven2/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2-sources.jar
Source1  : http://repo1.maven.org/maven2/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2.jar
Source2  : http://repo1.maven.org/maven2/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2.pom
Source3  : https://repo1.maven.org/maven2/org/jboss/integration-platform/jboss-integration-platform-parent/6.0.0.CR28/jboss-integration-platform-parent-6.0.0.CR28.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: mvn-jboss-logging-data = %{version}-%{release}
Requires: mvn-jboss-logging-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jboss-logging package.
Group: Data

%description data
data components for the mvn-jboss-logging package.


%package license
Summary: license components for the mvn-jboss-logging package.
Group: Default

%description license
license components for the mvn-jboss-logging package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jboss-logging
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-jboss-logging/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jboss/logging/jboss-logging/3.1.0.CR2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jboss/logging/jboss-logging/3.1.0.CR2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jboss/logging/jboss-logging/3.1.0.CR2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jboss/integration-platform/jboss-integration-platform-parent/6.0.0.CR28
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/jboss/integration-platform/jboss-integration-platform-parent/6.0.0.CR28/jboss-integration-platform-parent-6.0.0.CR28.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/jboss/integration-platform/jboss-integration-platform-parent/6.0.0.CR28/jboss-integration-platform-parent-6.0.0.CR28.pom
/usr/share/java/.m2/repository/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2-sources.jar
/usr/share/java/.m2/repository/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2.jar
/usr/share/java/.m2/repository/org/jboss/logging/jboss-logging/3.1.0.CR2/jboss-logging-3.1.0.CR2.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jboss-logging/LICENSE.txt
