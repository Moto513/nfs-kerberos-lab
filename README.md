# NFS with Kerberos Authentication Lab

This repository documents a complete setup for enabling Kerberos-authenticated NFSv4 file sharing using Ubuntu.

## Overview

- Hostname: `samba.lab`
- Realm: `LAB.LOCAL`
- Shared Directory: `/exports`
- Mount Point: `/mnt/exports`
- Authentication: Kerberos (`sec=krb5`)

## Important Files

| File | Description |
|------|-------------|
| krb5.conf | Kerberos configuration |
| kadm5.acl | Admin privileges for Kerberos |
| idmapd.conf | NFSv4 domain configuration |
| exports | NFSv4 export settings |

## Mount (Client Side)

```bash
kinit motokazu
sudo mount -t nfs4 -o sec=krb5 samba.lab:/ /mnt/exports
