# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class ProjectsCreateResponse(pydantic_v1.BaseModel):
    """
    Project
    """

    title: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Project title
    """

    description: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Project description
    """

    label_config: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Label config in XML format
    """

    expert_instruction: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Labeling instructions to show to the user
    """

    show_instruction: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Show labeling instructions
    """

    show_skip_button: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Show skip button
    """

    enable_empty_annotation: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Allow empty annotations
    """

    show_annotation_history: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Show annotation history
    """

    reveal_preannotations_interactively: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Reveal preannotations interactively. If set to True, predictions will be shown to the user only after selecting the area of interest
    """

    show_collab_predictions: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Show predictions to annotators
    """

    maximum_annotations: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    Maximum annotations per task
    """

    color: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Project color in HEX format
    """

    control_weights: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field(default=None)
    """
    Dict of weights for each control tag in metric calculation. Each control tag (e.g. label or choice) will have its own key in control weight dict with weight for each label and overall weight. For example, if a bounding box annotation with a control tag named my_bbox should be included with 0.33 weight in agreement calculation, and the first label Car should be twice as important as Airplane, then you need to specify: {'my_bbox': {'type': 'RectangleLabels', 'labels': {'Car': 1.0, 'Airplane': 0.5}, 'overall': 0.33}
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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
