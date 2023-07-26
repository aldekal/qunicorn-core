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


"""Module containing the root endpoint of the DEVICES API."""

from dataclasses import dataclass

from ..flask_api_utils import SecurityBlueprint as SmorestBlueprint

DEVICES_API = SmorestBlueprint(
    "device-api",
    "DEVICES API",
    description="Devices API to list available resources.",
    url_prefix="/devices/",
)


@dataclass()
class RootData:
    root: str
