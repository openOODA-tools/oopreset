Name:           oopreset
Version:        0.1.0
Release:        1%{?dist}
Summary:        Exports oote color schemes to Alacritty, Kitty, Foot, Ghostty, and Tmux formats.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oopreset
Source0:        oopreset-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oopreset is a sovereign, capability-bounded THEME PRESETS written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oopreset
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oopreset-uninstall

%files
/usr/bin/oopreset
/usr/bin/oopreset-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
