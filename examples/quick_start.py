"""Inspect the installed pack identity."""

from rbac_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:rbac"
print(metadata["origin"]["id"])
