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

# originally from <https://github.com/buehlefs/flask-template/>

from qunicorn_core.db.database_services import db_service
from qunicorn_core.db.models.user import UserDataclass
from qunicorn_core.api.api_models import UserDto


def get_all_users() -> list[UserDataclass]:
    """Gets all Users from the DB"""
    return db_service.get_all_database_objects(UserDataclass)


def get_user_by_id(user_id: int) -> UserDataclass:
    """Get a user by id"""
    return db_service.get_database_object_by_id(user_id, UserDataclass)


def get_default_user() -> UserDataclass:
    """Gets the Default User from the database"""
    return db_service.get_database_object_by_id(UserDto.get_default_user().id, UserDataclass)
