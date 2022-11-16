Ansible role ableton.prometheus_node_exporter
=============================================

This role installs [Prometheus `node_exporter`][node-exporter] as a service on the given
host. If the target system has a package manager with the `node_exporter` package, then
this role installs the software that way. Otherwise, the software will be built from
sources.

On Windows, this role installs [`windows_exporter`][windows-exporter].

Requirements
------------

Ansible >= 2.10 is required. This role supports package-based installation on the
following OS types:

- Debian Linux (via the `apt` module)
- macOS (via the `homebrew` module)
- Windows (via the `win_chocolatey` module)

For all other platforms, a source-based installation will be performed. On such systems
where package-based installation is *not* available, the following software is required:

- Go (golang)
- GNU Make

This role does *not* install either of the above software on the host; you must take care
to do that before applying this role.

Role Variables
--------------

The following role variables are used for `node_exporter`'s service configuration:

- `node_exporter_args`: A list of arguments to pass to the `node_exporter` service, one
  argument per list item.
- `node_exporter_group`: Group for the `node_exporter_user` user.
- `node_exporter_port`: Port to expose metrics on.
- `node_exporter_user`: User to run `node_exporter` as.

The following variables are used when building `node_exporter` from sources.

- `node_exporter_install_from_binary`: When `true`, `node_exporter` will be installed from
  a binary download and not via a package manager. This option is not supported on all
  system types (see the "Requirements" section above).
- `node_exporter_binary_arch`: Binary architecture to fetch when downloading the
  `node_exporter` binary.
- `node_exporter_version`: Version of node_exporter to install from source.

The following variables are used on Windows:

- `windows_exporter_version`: Version of windows_exporter to install using Chocolatey.

See the [`defaults/main.yml`](defaults/main.yml) file for full documentation on required
and optional role variables.

Example Playbook
----------------

```yaml
---
- name: Install node_exporter on hosts
  hosts: "all"
  vars:
    node_exporter_port: 9100
    node_exporter_binary_arch: "amd64"
    node_exporter_group: "{{ ansible_user }}"
    node_exporter_user: "{{ ansible_user }}"
    node_exporter_version: "0.18.1"

  pre_tasks:
    - name: Force macOS hosts to install from source, so a specific version can be used
      set_fact:
        node_exporter_install_from_binary: true
      when: ansible_os_family == "Darwin"

    - name: Install prerequisite software for macOS hosts
      homebrew:
        name: golang
        state: present

  roles:
    - ableton.prometheus_node_exporter
```

License
-------

MIT

Maintainers
-----------

This project is maintained by the following GitHub users:

- [@ala-ableton](https://github.com/ala-ableton)
- [@nre-ableton](https://github.com/nre-ableton)


[node-exporter]: https://github.com/prometheus/node_exporter
[windows-exporter]: https://github.com/prometheus-community/windows_exporter
