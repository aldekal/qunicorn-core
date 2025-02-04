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


"""Module containing all Dtos and their Schemas  for tasks in the Services API."""
from dataclasses import dataclass

import marshmallow as ma

from ..flask_api_utils import MaBaseSchema

__all__ = ["ProviderDtoSchema", "ProviderIDSchema", "ProviderDto"]


@dataclass
class ProviderDto:
    id: int
    with_token: bool
    supported_language: str
    name: str


class ProviderDtoSchema(MaBaseSchema):
    id = ma.fields.Integer(required=True, allow_none=False)
    with_token = ma.fields.Boolean(required=False, allow_none=True)
    supported_language = ma.fields.String(required=False, allow_none=True)
    name = ma.fields.String(required=True, allow_none=False)


class ProviderIDSchema(MaBaseSchema):
    provider_id = ma.fields.String(required=True, allow_none=False)
