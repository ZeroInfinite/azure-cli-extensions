# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer, StorageAccountPreparer, JMESPathCheck, NoneCheck,
                               api_version_constraint)
from azure.cli.core.profiles import ResourceType
from ...profiles import CUSTOM_FIREWALL


class AzureFirewallScenario(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_azure_firewall')
    def test_azure_firewall(self, resource_group):

        self.kwargs.update({
            'af': 'af1',
            'coll': 'rc1',
            'rule1': 'rule1',
            'rule2': 'rule2'
        })
        pass
