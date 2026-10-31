# Security Policy

## Supported versions

The hosted service at [tryhaircutai.com](https://tryhaircutai.com) is always the supported version. This repository (style library and site copy) has no separately supported releases.

## Reporting a vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, report them privately via [GitHub Security Advisories](https://github.com/OnlyBuild/tryhaircutai.com/security/advisories/new), or email **support@tryhaircutai.com** with the subject `Security report`.

Please include as much of the following as you can:

- Type of issue (e.g. auth bypass, IDOR, injection, credit-ledger manipulation)
- Full paths of affected endpoints or repository files
- Step-by-step reproduction, including any request bodies
- Proof-of-concept or exploit code
- Impact assessment, including how an attacker might chain the issue

## What counts as in scope

- The hosted application at `tryhaircutai.com` (auth, payments, credits, generation API)
- Cross-tenant access to render history or uploaded photos
- Credit bypass or ledger manipulation
- Anything in this repository's scripts that executes on contributor machines

## Out of scope

- Rate limiting / resource exhaustion without a demonstrated privacy or billing impact
- Reports from automated scanners without a working reproduction
- Self-hosted deployments misconfigured by their operators
- Social engineering of our staff or users

## Disclosure timeline

- We acknowledge reports within 72 hours
- Fixes for accepted issues ship as soon as practical; you'll be notified when the fix is live
- Coordinated disclosure after the fix, crediting you unless you prefer otherwise

We thank every responsible reporter — safe haircuts, safe software.
