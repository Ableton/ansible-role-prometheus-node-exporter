import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_node_exporter_binary(host):
    node_exporter_bin = host.file("/usr/bin/prometheus-node-exporter")

    assert node_exporter_bin.is_file
    assert node_exporter_bin.mode == 0o0755


def test_node_exporter_configuration(host):
    node_exporter_config = host.file("/etc/default/prometheus-node-exporter")

    assert node_exporter_config.is_file
    assert node_exporter_config.mode == 0o0644
    assert (
        node_exporter_config.content.decode()
        == "ARGS='--collector.arp --collector.cpu --web.listen-address=:9999'"
    )


def test_node_exporter_service(host):
    node_exporter_service = host.service("prometheus-node-exporter")

    assert node_exporter_service.is_enabled
    assert node_exporter_service.is_running
