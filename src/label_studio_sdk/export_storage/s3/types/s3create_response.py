# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class S3CreateResponse(pydantic_v1.BaseModel):
    can_delete_objects: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Deletion from storage enabled.
    """

    title: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Storage title
    """

    description: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Storage description
    """

    project: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Project ID
    """

    bucket: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    S3 bucket name
    """

    prefix: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    S3 bucket prefix
    """

    aws_access_key_id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    AWS_ACCESS_KEY_ID
    """

    aws_secret_access_key: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    AWS_SECRET_ACCESS_KEY
    """

    aws_session_token: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    AWS_SESSION_TOKEN
    """

    aws_sse_kms_key_id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    AWS SSE KMS Key ID
    """

    region_name: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    AWS Region
    """

    s3endpoint: typing.Optional[str] = pydantic_v1.Field(alias="s3_endpoint", default=None)
    """
    S3 Endpoint
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
