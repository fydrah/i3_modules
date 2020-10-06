# Py3Status modules (i3)

Check https://github.com/ultrabug/py3status for more information about Py3Status.

## Custom modules

Put these modules under your custom modules configuration. E.g:

```
status_command py3status -i ~/.config/i3status/ -i ~/.config/i3status/modules/ -c ~/.config/i3status/config
```

^ Put modules under ``~/.config/i3status/modules`` directory.

### GCloud

Print gcloud (google cloud) current context.

Usage:

```
order += "gcloud"
```

Output:

```
glcoud:default
```

### Kubernetes

Print Kubernetes current context and namespace.

Usage:

```
order += "kubecontext"
```

Output:

```
\u2388 CONTEXT_NAME:NAMESPACE
```

### VPN

Print active VPN managed by Network manager.

Usage:

```
order += "vpn"
```

Output:

```
VPN: None       # <<< no active vpn, in red
VPN: vpn-dublin # <<< "vpn-dublin" active, in green
```
