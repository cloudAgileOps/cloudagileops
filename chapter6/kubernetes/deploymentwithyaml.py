from os import path

from kubernetes import client, config, utils

import time

def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.

    with open('token.txt', 'r') as file:
        Token = file.read().strip('\n')

    APISERVER = 'https://10.142.0.2:6443'

    configuration = client.Configuration()

    configuration.host = APISERVER

    configuration.verify_ssl = False

    client.Configuration.set_default(configuration)

    k8s_client = client.ApiClient()

    k8s_coreapi = client.CoreV1Api(k8s_client)

    k8s_extendapi = client.ExtensionsV1beta1Api(k8s_client)

    utils.create_from_yaml(k8s_client, "deployment.yaml")

    deps = k8s_extendapi.read_namespaced_deployment("todolist", "default")

    print("Deployment {0} created".format(deps.metadata.name))


    i = 0
    while i < 10:
        pods = k8s_coreapi.list_namespaced_pod("default")

        host_ip = ""
        for item in pods.items:
            labels = item.metadata.labels
            for key in labels.keys():
                if key == "app":
                    if labels[key] == "todolist":
                        host_ip = item.status.host_ip

        if host_ip != None:
            break
        i = i+1
        time.sleep(10)


    utils.create_from_yaml(k8s_client, "service.yaml")

    services= k8s_coreapi.read_namespaced_service("todolist", "default")

    print("Serivces {0} created".format(services.metadata.name))

    print("Host IP is %s" % host_ip)
    print("NodePort is {0}".format(services.spec.ports[0].node_port))


if __name__ == '__main__':
    main()

