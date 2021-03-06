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

from ws_api_client.models.market import Market  # noqa: F401,E501


class Trim(object):
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
        'slug': 'str',
        'name': 'str',
        'trim': 'str',
        'body': 'str',
        'generation': 'str',
        'production_start_year': 'int',
        'production_end_year': 'int',
        'markets': 'list[Market]'
    }

    attribute_map = {
        'slug': 'slug',
        'name': 'name',
        'trim': 'trim',
        'body': 'body',
        'generation': 'generation',
        'production_start_year': 'production_start_year',
        'production_end_year': 'production_end_year',
        'markets': 'markets'
    }

    def __init__(self, slug=None, name=None, trim=None, body=None, generation=None, production_start_year=None, production_end_year=None, markets=None):  # noqa: E501
        """Trim - a model defined in Swagger"""  # noqa: E501

        self._slug = None
        self._name = None
        self._trim = None
        self._body = None
        self._generation = None
        self._production_start_year = None
        self._production_end_year = None
        self._markets = None
        self.discriminator = None

        if slug is not None:
            self.slug = slug
        if name is not None:
            self.name = name
        if trim is not None:
            self.trim = trim
        if body is not None:
            self.body = body
        if generation is not None:
            self.generation = generation
        if production_start_year is not None:
            self.production_start_year = production_start_year
        if production_end_year is not None:
            self.production_end_year = production_end_year
        if markets is not None:
            self.markets = markets

    @property
    def slug(self):
        """Gets the slug of this Trim.  # noqa: E501

        Combined trim, body, and generation identifier. Non-unique through markets (e.g. `20-gg2w-iii-restyling`)  # noqa: E501

        :return: The slug of this Trim.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Trim.

        Combined trim, body, and generation identifier. Non-unique through markets (e.g. `20-gg2w-iii-restyling`)  # noqa: E501

        :param slug: The slug of this Trim.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def name(self):
        """Gets the name of this Trim.  # noqa: E501

        Format: __*`trim (body) [generation]`*__ (e.g. `2.0 (GG2W) [III Restyling]`)  # noqa: E501

        :return: The name of this Trim.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Trim.

        Format: __*`trim (body) [generation]`*__ (e.g. `2.0 (GG2W) [III Restyling]`)  # noqa: E501

        :param name: The name of this Trim.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def trim(self):
        """Gets the trim of this Trim.  # noqa: E501

        Trim name. It can be empty for models created for JDM market (e.g. `2.0`, can be __*`null`*__)  # noqa: E501

        :return: The trim of this Trim.  # noqa: E501
        :rtype: str
        """
        return self._trim

    @trim.setter
    def trim(self, trim):
        """Sets the trim of this Trim.

        Trim name. It can be empty for models created for JDM market (e.g. `2.0`, can be __*`null`*__)  # noqa: E501

        :param trim: The trim of this Trim.  # noqa: E501
        :type: str
        """

        self._trim = trim

    @property
    def body(self):
        """Gets the body of this Trim.  # noqa: E501

        Body name. Used extensively for JDM market (e.g. `GG2W`, can be __*`null`*__)  # noqa: E501

        :return: The body of this Trim.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Trim.

        Body name. Used extensively for JDM market (e.g. `GG2W`, can be __*`null`*__)  # noqa: E501

        :param body: The body of this Trim.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def generation(self):
        """Gets the generation of this Trim.  # noqa: E501

        Generation name (e.g. `III Restyling`, can be __*`null`*__)  # noqa: E501

        :return: The generation of this Trim.  # noqa: E501
        :rtype: str
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this Trim.

        Generation name (e.g. `III Restyling`, can be __*`null`*__)  # noqa: E501

        :param generation: The generation of this Trim.  # noqa: E501
        :type: str
        """

        self._generation = generation

    @property
    def production_start_year(self):
        """Gets the production_start_year of this Trim.  # noqa: E501

        Trim production start year (e.g. `2015`, can be __*`null`*__)  # noqa: E501

        :return: The production_start_year of this Trim.  # noqa: E501
        :rtype: int
        """
        return self._production_start_year

    @production_start_year.setter
    def production_start_year(self, production_start_year):
        """Sets the production_start_year of this Trim.

        Trim production start year (e.g. `2015`, can be __*`null`*__)  # noqa: E501

        :param production_start_year: The production_start_year of this Trim.  # noqa: E501
        :type: int
        """

        self._production_start_year = production_start_year

    @property
    def production_end_year(self):
        """Gets the production_end_year of this Trim.  # noqa: E501

        Trim production end year (e.g. `2016`, can be __*`null`*__)  # noqa: E501

        :return: The production_end_year of this Trim.  # noqa: E501
        :rtype: int
        """
        return self._production_end_year

    @production_end_year.setter
    def production_end_year(self, production_end_year):
        """Sets the production_end_year of this Trim.

        Trim production end year (e.g. `2016`, can be __*`null`*__)  # noqa: E501

        :param production_end_year: The production_end_year of this Trim.  # noqa: E501
        :type: int
        """

        self._production_end_year = production_end_year

    @property
    def markets(self):
        """Gets the markets of this Trim.  # noqa: E501

        List of markets where this trim if present  # noqa: E501

        :return: The markets of this Trim.  # noqa: E501
        :rtype: list[Market]
        """
        return self._markets

    @markets.setter
    def markets(self, markets):
        """Sets the markets of this Trim.

        List of markets where this trim if present  # noqa: E501

        :param markets: The markets of this Trim.  # noqa: E501
        :type: list[Market]
        """

        self._markets = markets

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
        if not isinstance(other, Trim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
