# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401

from petstore_api import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401
import uuid  # noqa: F401

from petstore_api import schemas  # noqa: F401

from . import path

# query params


class MapBeanSchema(
    schemas.DictSchema
):


    class MetaOapg:
        class properties:
            keyword = schemas.StrSchema
        additional_properties = schemas.AnyTypeSchema
    
    keyword: MetaOapg.properties.keyword

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        keyword: typing.Union[MetaOapg.properties.keyword, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'MapBeanSchema':
        return super().__new__(
            cls,
            *args,
            keyword=keyword,
            _configuration=_configuration,
            **kwargs,
        )
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'mapBean': typing.Union[MapBeanSchema, dict, frozendict, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_map_bean = api_client.QueryParameter(
    name="mapBean",
    style=api_client.ParameterStyle.DEEP_OBJECT,
    schema=MapBeanSchema,
    explode=True,
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
)
_status_code_to_response = {
    '200': _response_for_200,
}


class BaseApi(api_client.Api):

    def _object_in_query(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        user list
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_map_bean,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
        # TODO add cookie handling

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class ObjectInQuery(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def object_in_query(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._object_in_query(
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(
        self: BaseApi,
        query_params: RequestQueryParams = frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        return self._object_in_query(
            query_params=query_params,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

