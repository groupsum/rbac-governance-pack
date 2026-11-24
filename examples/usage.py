"""Find a specification and its downstream path in the installed manifest."""

from rbac_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:rbac-core-role-permission-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-rbac-core-role-permission-contract.yaml"
