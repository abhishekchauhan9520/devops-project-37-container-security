# Project 37 — Container Security & Image Scanning

Standalone container-security lab for hardening images and validating container runtime posture.

## Security controls

- Minimal Python runtime image
- Pinned base image digest in the hardened Dockerfile
- Non-root user
- Read-only root filesystem at runtime
- No privilege escalation
- All Linux capabilities dropped
- `no-new-privileges`
- Resource limits in Compose
- Secret and config hygiene checks
- Trivy vulnerability scan
- Grype vulnerability scan
- CycloneDX SBOM generation
- Syft SBOM generation
- Dockerfile lint/security checks with Hadolint
- Runtime configuration assertions
- CI fail-closed security gates

## Scan policy

Critical vulnerabilities fail the gate. High vulnerabilities fail when a fixed version is available. Unfixed findings are reported separately and do not silently disappear.

## Runtime

The Compose example uses a non-root container with a read-only root filesystem and explicit writable `tmpfs` only where the application needs temporary files.

## Verification

Docker/OCI tooling must be available to run the live image build and vulnerability scans. GitHub Actions performs the authoritative scan workflow.
