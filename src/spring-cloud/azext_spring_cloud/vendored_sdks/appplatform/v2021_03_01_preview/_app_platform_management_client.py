# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AppPlatformManagementClientConfiguration
from .operations import TanzuServicesOperations
from .operations import AppsOperations
from .operations import DeploymentsOperations
from .operations import BuildServiceOperations
from .operations import ConfigurationServicesOperations
from . import models


class AppPlatformManagementClient(SDKClient):
    """REST API for Azure Spring Cloud Tanzu

    :ivar config: Configuration for client.
    :vartype config: AppPlatformManagementClientConfiguration

    :ivar tanzu_services: TanzuServices operations
    :vartype tanzu_services: azure.mgmt.appplatform.v2021_03_01_preview.operations.TanzuServicesOperations
    :ivar apps: Apps operations
    :vartype apps: azure.mgmt.appplatform.v2021_03_01_preview.operations.AppsOperations
    :ivar deployments: Deployments operations
    :vartype deployments: azure.mgmt.appplatform.v2021_03_01_preview.operations.DeploymentsOperations
    :ivar build_service: BuildService operations
    :vartype build_service: azure.mgmt.appplatform.v2021_03_01_preview.operations.BuildServiceOperations
    :ivar configuration_services: ConfigurationServices operations
    :vartype configuration_services: azure.mgmt.appplatform.v2021_03_01_preview.operations.ConfigurationServicesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription ID which uniquely identify the
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AppPlatformManagementClientConfiguration(credentials, subscription_id, base_url)
        super(AppPlatformManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2021-03-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.tanzu_services = TanzuServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.apps = AppsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.deployments = DeploymentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.build_service = BuildServiceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.configuration_services = ConfigurationServicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
