# coding: utf-8

"""
    Wheel Fitment API

    The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@wheel-size.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ws_api_client.models.generation import Generation  # noqa: F401,E501
from ws_api_client.models.make import Make  # noqa: F401,E501
from ws_api_client.models.model import Model  # noqa: F401,E501
from ws_api_client.models.rim_agregation import RimAgregation  # noqa: F401,E501
from ws_api_client.models.tires_aggregation import TiresAggregation  # noqa: F401,E501


class ModelWithTires(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'make': 'Make',
        'model': 'Model',
        'year': 'int',
        'years': 'list[int]',
        'generations': 'list[Generation]',
        'tires': 'TiresAggregation',
        'rims': 'dict(str, RimAgregation)'
    }

    attribute_map = {
        'make': 'make',
        'model': 'model',
        'year': 'year',
        'years': 'years',
        'generations': 'generations',
        'tires': 'tires',
        'rims': 'rims'
    }

    def __init__(self, make=None, model=None, year=None, years=None, generations=None, tires=None, rims=None):  # noqa: E501
        """ModelWithTires - a model defined in Swagger"""  # noqa: E501

        self._make = None
        self._model = None
        self._year = None
        self._years = None
        self._generations = None
        self._tires = None
        self._rims = None
        self.discriminator = None

        if make is not None:
            self.make = make
        if model is not None:
            self.model = model
        if year is not None:
            self.year = year
        if years is not None:
            self.years = years
        if generations is not None:
            self.generations = generations
        if tires is not None:
            self.tires = tires
        if rims is not None:
            self.rims = rims

    @property
    def make(self):
        """Gets the make of this ModelWithTires.  # noqa: E501


        :return: The make of this ModelWithTires.  # noqa: E501
        :rtype: Make
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this ModelWithTires.


        :param make: The make of this ModelWithTires.  # noqa: E501
        :type: Make
        """

        self._make = make

    @property
    def model(self):
        """Gets the model of this ModelWithTires.  # noqa: E501


        :return: The model of this ModelWithTires.  # noqa: E501
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ModelWithTires.


        :param model: The model of this ModelWithTires.  # noqa: E501
        :type: Model
        """

        self._model = model

    @property
    def year(self):
        """Gets the year of this ModelWithTires.  # noqa: E501

        Selected year (e.g. `2015`, can be __*`null`*__)  # noqa: E501

        :return: The year of this ModelWithTires.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this ModelWithTires.

        Selected year (e.g. `2015`, can be __*`null`*__)  # noqa: E501

        :param year: The year of this ModelWithTires.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def years(self):
        """Gets the years of this ModelWithTires.  # noqa: E501

        Model production years  # noqa: E501

        :return: The years of this ModelWithTires.  # noqa: E501
        :rtype: list[int]
        """
        return self._years

    @years.setter
    def years(self, years):
        """Sets the years of this ModelWithTires.

        Model production years  # noqa: E501

        :param years: The years of this ModelWithTires.  # noqa: E501
        :type: list[int]
        """

        self._years = years

    @property
    def generations(self):
        """Gets the generations of this ModelWithTires.  # noqa: E501


        :return: The generations of this ModelWithTires.  # noqa: E501
        :rtype: list[Generation]
        """
        return self._generations

    @generations.setter
    def generations(self, generations):
        """Sets the generations of this ModelWithTires.


        :param generations: The generations of this ModelWithTires.  # noqa: E501
        :type: list[Generation]
        """

        self._generations = generations

    @property
    def tires(self):
        """Gets the tires of this ModelWithTires.  # noqa: E501


        :return: The tires of this ModelWithTires.  # noqa: E501
        :rtype: TiresAggregation
        """
        return self._tires

    @tires.setter
    def tires(self, tires):
        """Sets the tires of this ModelWithTires.


        :param tires: The tires of this ModelWithTires.  # noqa: E501
        :type: TiresAggregation
        """

        self._tires = tires

    @property
    def rims(self):
        """Gets the rims of this ModelWithTires.  # noqa: E501

        Each key is bolt pattern, e.g. *`5x105`*  # noqa: E501

        :return: The rims of this ModelWithTires.  # noqa: E501
        :rtype: dict(str, RimAgregation)
        """
        return self._rims

    @rims.setter
    def rims(self, rims):
        """Sets the rims of this ModelWithTires.

        Each key is bolt pattern, e.g. *`5x105`*  # noqa: E501

        :param rims: The rims of this ModelWithTires.  # noqa: E501
        :type: dict(str, RimAgregation)
        """

        self._rims = rims

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelWithTires):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
