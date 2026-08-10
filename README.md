# rbac-governance-pack

Governance for RBAC users, roles, permissions, assignments, activation, hierarchies, separation of duty, entitlement normalization, review, and audit evidence.

## Package identity

- Pack ID: `pack:rbac`
- PyPI distribution: `rbac-governance-pack`
- Python import: `rbac_governance_pack`
- Reservation owner: `extension-pack:rbac-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add rbac-governance-pack
uv run ssot pack sync . rbac_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://csrc.nist.gov/Projects/Role-Based-Access-Control
