# ls ../../nimbleclient/v1/api/*[a-z].py | xargs basename | sed 's#\.py$##' | tr \\n ' '

apis = access_control_records active_directory_memberships alarms application_categories application_servers arrays audit_log chap_users controllers disks events fibre_channel_configs fibre_channel_initiator_aliases fibre_channel_interfaces fibre_channel_ports fibre_channel_sessions folders groups initiator_groups initiators jobs key_managers master_key network_configs network_interfaces performance_policies pools protection_schedules protection_templates protocol_endpoints replication_partners shelves snapshot_collections snapshots software_versions space_domains subnets support tokens user_groups user_policies users versions volume_collections volumes witnesses
class = nimbleclient.v1.api

gen:
	for api in $(apis); do pydocmd simple $(class).$${api}+ > $${api}.md;done
	for api in $(apis); do echo "    - '$${api}': 'api/$${api}.md'";done

single:
	rm -f api.md || true
	for api in $(apis); do pydocmd simple $(class).$${api}+ >> api.md;done
