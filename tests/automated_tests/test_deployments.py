# Copyright 2023 University of Stuttgart
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""""Test class to test the functionality of the job_api"""

from qunicorn_core.api.api_models import DeploymentRequestDto
from qunicorn_core.core import deployment_service
from qunicorn_core.db.database_services import deployment_db_service
from qunicorn_core.db.models.deployment import DeploymentDataclass
from qunicorn_core.static.enums.provider_name import ProviderName
from tests import test_utils
from tests.conftest import set_up_env

DEPLOYMENT_NAME = "DeploymentName"
PROGRAM_NUMBER = 2


def test_create_deployments():
    """Testing if the creation of deployments works"""
    # GIVEN: Get Deployments from JSON
    app = set_up_env()
    deployment: DeploymentRequestDto = test_utils.get_test_deployment_request(ProviderName.IBM)

    # WHEN: Create deployment and save it in the db
    with app.app_context():
        depl_id: int = deployment_service.create_deployment(deployment).id

    # THEN: Test if the name and number of programs is correct
    with app.app_context():
        deployment: DeploymentDataclass = deployment_db_service.get_deployment_by_id(depl_id)
        assert deployment.name == DEPLOYMENT_NAME
        assert len(deployment.programs) == PROGRAM_NUMBER
