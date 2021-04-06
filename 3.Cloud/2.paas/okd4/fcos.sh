alias coreos-installer='podman run --pull=always            \
                        --rm --tty --interactive            \
                        --security-opt label=disable        \
                        --volume ${PWD}:/pwd --workdir /pwd \
                        quay.io/coreos/coreos-installer:release'

alias ignition-validate='podman run --rm --tty --interactive \
                         --security-opt label=disable        \
                         --volume ${PWD}:/pwd --workdir /pwd \
                         quay.io/coreos/ignition-validate:release'

alias fcct='podman run --rm --tty --interactive \
            --security-opt label=disable        \
            --volume ${PWD}:/pwd --workdir /pwd \
            quay.io/coreos/fcct:release'
