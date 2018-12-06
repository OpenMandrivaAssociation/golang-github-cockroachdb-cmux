# http://github.com/cockroachdb/cmux
%global goipath         github.com/cockroachdb/cmux
%global commit          30d10be492927e2dcae0089c374c455d42414fcb

%gometa

Name:           %{goname}
Version:        0
Release:        0.13%{?dist}
Summary:        Connection mux for serving different services on the same port
# Detected licences
# - *No copyright* UNKNOWN at 'LICENSE'
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/net/http2)
BuildRequires: golang(golang.org/x/net/http2/hpack)
# Tests deps
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/websocket)
BuildRequires: golang(google.golang.org/grpc)
# BuildRequires: golang(google.golang.org/grpc/examples/helloworld/helloworld)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Wed Nov 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.13.20181114git30d10be
- Bump to commit 30d10be492927e2dcae0089c374c455d42414fcb

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.12.git112f050
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git112f050
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git112f050
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git112f050
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git112f050
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git112f050
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git112f050
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git112f050
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.4.git112f050
- Polish the spec file
  related: #1387177

* Thu Oct 20 2016 jchaloup <jchaloup@redhat.com> - 0-0.3.git112f050
- skip tests
  resolves: #1387177

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git112f050
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun May 15 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git112f050
- First package for Fedora
  resolves: #1336218
