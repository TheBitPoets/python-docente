# GitHub Actions recovery + P1 Docker consumer strategy — 2026-08-27

## Status

`python-docente#8` is resolved.

After `TheBitPoets/python-docente` became public, the existing hosted-runner workflow started executing real steps instead of failing pre-runner with `steps=null`.

Current real evidence from run `33085594545` / #337 on head family `7011e4c66ee78a78309482eb25dcab47659c8f60`:

```text
Ubuntu  Python 3.12 setup                     PASS
Windows Python 3.12 setup                     PASS
Ubuntu  unified static course QA              PASS
Windows unified static course QA              PASS
Ubuntu  pinned TheBitLab checkout             PASS
Windows pinned TheBitLab checkout             PASS
Ubuntu  Course Workspace round-trip           PASS
Windows Course Workspace round-trip           PASS
Ubuntu  managed Activity assignment           PASS
Windows managed Activity assignment           PASS
Ubuntu  host P1 consumer smoke                PASS
Windows host P1 consumer smoke                PASS
```

The previous infrastructure classification is therefore closed: Actions now execute normally.

## Remaining consumer-workflow finding

The Ubuntu job then failed while pulling the assignment-runner release from GHCR:

```text
ghcr.io/thebitpoets/2cornot2c-assignment-runner@sha256:62f0...e159
→ manifest unknown

version tag 2026.07.1
→ denied
```

Authentication itself succeeded. This is a distribution/access property of the GHCR package, not a failure of the M04/P1 Activity contract.

The locked toolchain record at the pinned TheBitLab consumer baseline contains:

```text
toolchain version   2026.07.1
platform            linux/amd64
runner source       bd102146a684a9b06835204ec1b7f668f7655a03
release lock        ghcr.io/thebitpoets/2cornot2c-assignment-runner@sha256:62f0f7b7bc1d48d01b7f8e5fa765e0b43be3622e70a614033b1bb4a4e522e159
```

The source revision contains the reproducible assignment-runner build manifest with a digest-pinned Debian base image, Debian snapshot, exact package versions, worker schema and OCI label checks.

## Decision

The P1 CI consumer no longer requires the published GHCR artifact to be accessible.

Authoritative CI execution now uses:

```text
pinned course consumer baseline
  cdcdf4a6c9a3b1e28cc0a9702ca4f69a521849b0

lock → runner source revision
  bd102146a684a9b06835204ec1b7f668f7655a03

checkout exact runner source
→ scripts/build_assignment_runner.py
→ validate manifest + OCI labels + source revision
→ local image tag
  thebitlab-assignment-runner:p1-canary-2026.07.1
→ Docker P1 grading
```

The GHCR digest remains recorded as **release-lock provenance**. It is not silently replaced by another mutable package tag.

This is stricter than falling back to `latest` or to a version tag: the Docker image is built from the exact locked source revision and exact reproducible manifest, then its generated metadata is checked before grading.

## Evidence boundaries

A green source-built Docker run proves the P1 software/Docker contract for this pinned toolchain.

It still does **not** prove:

- final classroom-profile rehearsal;
- teacher sign-off;
- Content Pack 1.0 approval;
- general P2/P3/P4 certification;
- full course classroom readiness.

Those remain independent gates.
