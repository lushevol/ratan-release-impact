---
type: query
title: What Are the Approved MinIO RPO, RTO, and Capacity Targets for Indonesia?
created: 2026-08-24
updated: 2026-08-24
tags: [minio, nfr, rpo, rto, capacity, performance]
related: [minio, minio-cross-site-disaster-recovery, cash-settlement-dc-failover-strategy]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Minio Solutioning.md"]
---
# What Are the Approved MinIO RPO, RTO, and Capacity Targets for Indonesia?

The source proposes 500 MB/s cluster upload throughput, 99.99% availability, 11-nines durability, sub-30-second cross-site RPO, and sub-15-minute site RTO. It does not supply capacity modelling, failure tests, network measurements, topology assumptions, or ownership.

Establish approved targets based on payload volume and distribution, retention, concurrent traffic, replication bandwidth, erasure-set design, backup recovery tests, and coordinated platform failover tests.