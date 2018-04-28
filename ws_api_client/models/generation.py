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

from ws_api_client.models.body import Body  # noqa: F401,E501


class Generation(object):
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
        'name': 'str',
        'bodies': 'list[Body]',
        'start_year': 'int',
        'end_year': 'int',
        'years': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'bodies': 'bodies',
        'start_year': 'start_year',
        'end_year': 'end_year',
        'years': 'years'
    }

    def __init__(self, name=None, bodies=None, start_year=None, end_year=None, years=None):  # noqa: E501
        """Generation - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._bodies = None
        self._start_year = None
        self._end_year = None
        self._years = None
        self.discriminator = None

        self.name = name
        self.bodies = bodies
        if start_year is not None:
            self.start_year = start_year
        if end_year is not None:
            self.end_year = end_year
        if years is not None:
            self.years = years

    @property
    def name(self):
        """Gets the name of this Generation.  # noqa: E501

        Generation name (e.g. `III Restyling`)  # noqa: E501

        :return: The name of this Generation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Generation.

        Generation name (e.g. `III Restyling`)  # noqa: E501

        :param name: The name of this Generation.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def bodies(self):
        """Gets the bodies of this Generation.  # noqa: E501


        :return: The bodies of this Generation.  # noqa: E501
        :rtype: list[Body]
        """
        return self._bodies

    @bodies.setter
    def bodies(self, bodies):
        """Sets the bodies of this Generation.


        :param bodies: The bodies of this Generation.  # noqa: E501
        :type: list[Body]
        """
        if bodies is None:
            raise ValueError("Invalid value for `bodies`, must not be `None`")  # noqa: E501

        self._bodies = bodies

    @property
    def start_year(self):
        """Gets the start_year of this Generation.  # noqa: E501

        Generation start year  # noqa: E501

        :return: The start_year of this Generation.  # noqa: E501
        :rtype: int
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """Sets the start_year of this Generation.

        Generation start year  # noqa: E501

        :param start_year: The start_year of this Generation.  # noqa: E501
        :type: int
        """

        self._start_year = start_year

    @property
    def end_year(self):
        """Gets the end_year of this Generation.  # noqa: E501

        Generation end year. It equals to the __*`current year + 1`*__ if it is still in production.  # noqa: E501

        :return: The end_year of this Generation.  # noqa: E501
        :rtype: int
        """
        return self._end_year

    @end_year.setter
    def end_year(self, end_year):
        """Sets the end_year of this Generation.

        Generation end year. It equals to the __*`current year + 1`*__ if it is still in production.  # noqa: E501

        :param end_year: The end_year of this Generation.  # noqa: E501
        :type: int
        """

        self._end_year = end_year

    @property
    def years(self):
        """Gets the years of this Generation.  # noqa: E501

        Generation production years  # noqa: E501

        :return: The years of this Generation.  # noqa: E501
        :rtype: list[int]
        """
        return self._years

    @years.setter
    def years(self, years):
        """Sets the years of this Generation.

        Generation production years  # noqa: E501

        :param years: The years of this Generation.  # noqa: E501
        :type: list[int]
        """

        self._years = years

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
        if not isinstance(other, Generation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
