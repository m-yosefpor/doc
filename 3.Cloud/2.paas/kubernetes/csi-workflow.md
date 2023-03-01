1. pod referencing a volume is created
2. scheduler checks the volume exists or not, if not pod gets pending
3. if volume exists, scheduler checks storageClass of the volume. Look ups csiNode and found which node is capable of providing that storageClass, and choose one among them based on scoring and schedules it
4. attach-detach (a/d) controller in kube-controller-manager creates a volumeattachment object which tells the volume X should be attached to server Y >> check it manually `oc get volumeattahcment -oyaml | grep <pv-name> -C 30`
5. csi-attacher  container in snappcloud-stroage/csi-controller pod, will watch volumeattachments, and when a new volumeattachment is created, it executes a gRPC call (ControllerPublishVolume) to csi-driver container (a side-car container in same pod) to attach volume X to volume Y
6. csi-driver (in our case cinder-csi-driver) will translate ControllerPublishVolume csi.proto gRPC call to cinder rest HTTP api call (sth like openstack server add volume X Y)
7. cinder attaches volumes and returns HTTP status code
8. if ok, cinder-csi-driver response ok to csi-attacher
9. csi-attacher changes the status of the volumeattachment  "attached: true" and "status.attachmentMetadata.DevicePath: /dev/sdX" >>> you can verify with lsblk in node
10. a/d controller publishes an event on pod  that volume attach succeeded. >> you can view in describe pod
11. kubelet will continue with issuing a gRPC call NodeStageVolume to cinder-csi-driver in cinder csi-nodeplugin pods (daemonset on nodes) on /csi/csi.sock
12. csi-driver plugin will return return the volume ID
13. kubelet will  issue a gRPC call NodePublishVolume
14. csi-driver will use volume id to mount the volume >> you can verify with lsblk that the volume is mounted in /var/lib/kubelet/pods/<pod-id>/volumes/kubernetes.io~csi/<pv-name>/mount
15. csi-driver will recursively chowns files  with walk on file trees if pod .spec.securityContext.fsGroupChangePolicy is Always (default behavior if not set), or only applies recureive chown if the root directory current permission differs from what fsGroup is set in pod.spec if pod .spec.securityContext.fsGroupChangePolicy is OnRootMismatch
16. csi-driver check CSIDriver.spec.SELinuxMountSupported and if true it will mount directly with selinux context. Other was if false (dafault) will recursively chcon all files to match securityContext.seLinuxOptions.level
17. during the process kubelet if it takes over 2m, kubelet will emit a log on timeout mounting but it's ok it will retry checking again until the process is fully completed. >> only if you verifies step 14, you can w8 without worrying.
18. after mounting finishes, the kubelet will continue to create pods (other steps)
