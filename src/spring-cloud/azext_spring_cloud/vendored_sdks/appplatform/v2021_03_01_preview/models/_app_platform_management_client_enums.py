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

from enum import Enum


class ProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    deleted = "Deleted"
    succeeded = "Succeeded"
    failed = "Failed"
    moving = "Moving"
    moved = "Moved"
    move_failed = "MoveFailed"


class AppResourceProvisioningState(str, Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    creating = "Creating"
    updating = "Updating"


class DeploymentResourceProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    succeeded = "Succeeded"
    failed = "Failed"


class DeploymentResourceStatus(str, Enum):

    stopped = "Stopped"
    running = "Running"


class ConfigurationServiceProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    succeeded = "Succeeded"
    failed = "Failed"
    deleting = "Deleting"
    deleted = "Deleted"


class BuildResultProvisioningState(str, Enum):

    queuing = "Queuing"
    building = "Building"
    succeeded = "Succeeded"
    failed = "Failed"
    deleting = "Deleting"
    deleted = "Deleted"
