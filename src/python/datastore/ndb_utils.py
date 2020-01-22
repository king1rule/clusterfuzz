# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""NDB utilities. Provides utility functions for NDB."""

DEFAULT_BATCH_SIZE = 1000


def is_true(boolean_prop):
  """Helper for boolean property filters to avoid lint errors."""
  return boolean_prop == True  # pylint: disable=g-explicit-bool-comparison,singleton-comparison


def is_false(boolean_prop):
  """Helper for boolean property filters to avoid lint errors."""
  return boolean_prop == False  # pylint: disable=g-explicit-bool-comparison,singleton-comparison


def get_all_from_model(model):
  """Get all results from a ndb.Model."""
  return get_all_from_query(model.query())


def get_all_from_query(query, **kwargs):
  """Return all entities based on the query by paging, to avoid query
  expirations on App Engine."""
  # TODO(ochang): Queries no longer expire with new NDB. Remove this and all
  # fix up callers.
  kwargs.pop('batch_size', None)  # No longer supported.
  for entity in query.iter(**kwargs):
    yield entity
