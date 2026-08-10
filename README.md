<div align="center">

# rbac-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/rbac-governance-pack.svg)](https://pypi.org/project/rbac-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/rbac-governance-pack.svg)](https://pypi.org/project/rbac-governance-pack/)
[![License](https://img.shields.io/pypi/l/rbac-governance-pack.svg)](https://pypi.org/project/rbac-governance-pack/)
[![CI](https://github.com/groupsum/rbac-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/groupsum/rbac-governance-pack/actions/workflows/ci.yml)
[![Publish](https://github.com/groupsum/rbac-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/rbac-governance-pack/actions/workflows/publish.yml)

</div>

Governance for RBAC users, roles, permissions, assignments, activation, hierarchies, separation of duty, entitlement normalization, review, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `rbac-governance-pack` is an installable SSOT governance pack for Role-Based Access Control. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for role-based access control, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`rbac-governance-pack`](https://pypi.org/project/rbac-governance-pack/)
- GitHub package repository: [`groupsum/rbac-governance-pack`](https://github.com/groupsum/rbac-governance-pack)
- Import package: `rbac_governance_pack`
- 3 portable downstream ADR templates for governed decisions.
- 6 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:rbac`
- PyPI package: `rbac-governance-pack`
- Import package: `rbac_governance_pack`
- GitHub repository: [groupsum/rbac-governance-pack](https://github.com/groupsum/rbac-governance-pack)
- Reservation owner: `extension-pack:rbac-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

Role-Based Access Control

## Authority Sources

- [NIST Role-Based Access Control](https://csrc.nist.gov/Projects/Role-Based-Access-Control)

## Included ADRs

- [`adr:roles-are-permission-bundles-not-policy-truth`](https://github.com/groupsum/rbac-governance-pack/blob/master/src/rbac_governance_pack/templates/adr/ADR-1000-roles-are-permission-bundles-not-policy-truth.yaml) - Roles Are Permission Bundles Not Policy Truth
- [`adr:role-hierarchies-and-separation-of-duty-are-explicit`](https://github.com/groupsum/rbac-governance-pack/blob/master/src/rbac_governance_pack/templates/adr/ADR-1001-role-hierarchies-and-separation-of-duty-are-explicit.yaml) - Role Hierarchies And Separation Of Duty Are Explicit
- [`adr:entitlements-are-inputs-not-runtime-role-decisions`](https://github.com/groupsum/rbac-governance-pack/blob/master/src/rbac_governance_pack/templates/adr/ADR-1002-entitlements-are-inputs-not-runtime-role-decisions.yaml) - Entitlements Are Inputs Not Runtime Role Decisions

## Included SPECs

- [`spc:rbac-core-role-permission-contract`](https://github.com/groupsum/rbac-governance-pack/blob/master/src/rbac_governance_pack/templates/specs/SPEC-2000-rbac-core-role-permission-contract.yaml) - RBAC Core Role Permission Contract
- [`spc:user-role-and-permission-role-assignment-contract`](https://github.com/groupsum/rbac-governance-pack/blob/master/src/rbac_governance_pack/templates/specs/SPEC-2001-user-role-and-permission-role-assignment-contract.yaml) - User Role And Permission Role Assignment Contract
- [`spc:role-hierarchy-contract`](https://github.com/groupsum/rbac-governance-pack/blob/master/src/rbac_governance_pack/templates/specs/SPEC-2002-role-hierarchy-contract.yaml) - Role Hierarchy Contract
- [`spc:static-and-dynamic-separation-of-duty-contract`](https://github.com/groupsum/rbac-governance-pack/blob/master/src/rbac_governance_pack/templates/specs/SPEC-2003-static-and-dynamic-separation-of-duty-contract.yaml) - Static And Dynamic Separation Of Duty Contract
- [`spc:entitlement-role-and-group-normalization-contract`](https://github.com/groupsum/rbac-governance-pack/blob/master/src/rbac_governance_pack/templates/specs/SPEC-2004-entitlement-role-and-group-normalization-contract.yaml) - Entitlement Role And Group Normalization Contract
- [`spc:rbac-review-and-audit-contract`](https://github.com/groupsum/rbac-governance-pack/blob/master/src/rbac_governance_pack/templates/specs/SPEC-2005-rbac-review-and-audit-contract.yaml) - RBAC Review And Audit Contract

## Install With uv

```bash
uv add rbac-governance-pack
uv add ssot-registry rbac-governance-pack
```

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect rbac_governance_pack
uvx --from ssot-registry ssot pack preflight . rbac_governance_pack --all
uvx --from ssot-registry ssot pack sync . rbac_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from rbac_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-rbac-core-role-permission-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/rbac-governance-pack](https://github.com/groupsum/rbac-governance-pack)
- PyPI package: [rbac-governance-pack](https://pypi.org/project/rbac-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the role-based access control governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
