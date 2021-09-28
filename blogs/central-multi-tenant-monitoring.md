each team prometheus

prometheus operator , ease deployment/operation , composable config, resource inefficient.
collect all metrics, HA -> thanos
multi-tenancy challenge
SM namespace label (OPA?), kube-rbac-proxy, prom-label-proxy, promtheus
sa in project-template -> namespace-config-operator
connect to grafana
label queries in grafana -> allowed path + --enable-label-apis -> immutable cluster-monitoring-operator , CVO -> custom thanos

federating to other PMs -> /federate thanos, remote write -> thanso federate proxy

each namespace separate
each namespace as separate data source -> regex (org based)
