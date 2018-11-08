Prometheus Node Exporter Role
=============================

This role installs and starts the [Prometheus `node_exporter`][node-exporter]
service on an Ansible host. If the target system has a package manager with the
`node_exporter` package, then this role installs the software that way.
Otherwise, the software will be built from sources.


Supported Host OS Types
-----------------------

This role supports package-based installation on the following OS types:

- Debian Linux (via the `apt` module)
- Mac OS X (via `go get`)
- Windows (via the `win_chocolatey` module)

For all other platforms, a source-based installation will be performed.


Requirements
------------

For systems where package-based installation is *not* available, the following
software is required:

- Go (golang)
- GNU Make


[node-exporter]: https://github.com/prometheus/node_exporter
