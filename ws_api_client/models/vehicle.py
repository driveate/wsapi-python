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
from ws_api_client.models.market import Market  # noqa: F401,E501
from ws_api_client.models.power import Power  # noqa: F401,E501
from ws_api_client.models.wheel_pair import WheelPair  # noqa: F401,E501


class Vehicle(object):
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
        'market': 'Market',
        'body': 'str',
        'trim': 'str',
        'generation': 'Generation',
        'stud_holes': 'int',
        'pcd': 'float',
        'centre_bore': 'float',
        'lock_type': 'str',
        'lock_text': 'str',
        'bolt_pattern': 'str',
        'power': 'Power',
        'fuel': 'str',
        'wheels': 'list[WheelPair]'
    }

    attribute_map = {
        'market': 'market',
        'body': 'body',
        'trim': 'trim',
        'generation': 'generation',
        'stud_holes': 'stud_holes',
        'pcd': 'pcd',
        'centre_bore': 'centre_bore',
        'lock_type': 'lock_type',
        'lock_text': 'lock_text',
        'bolt_pattern': 'bolt_pattern',
        'power': 'power',
        'fuel': 'fuel',
        'wheels': 'wheels'
    }

    def __init__(self, market=None, body=None, trim=None, generation=None, stud_holes=None, pcd=None, centre_bore=None, lock_type=None, lock_text=None, bolt_pattern=None, power=None, fuel=None, wheels=None):  # noqa: E501
        """Vehicle - a model defined in Swagger"""  # noqa: E501

        self._market = None
        self._body = None
        self._trim = None
        self._generation = None
        self._stud_holes = None
        self._pcd = None
        self._centre_bore = None
        self._lock_type = None
        self._lock_text = None
        self._bolt_pattern = None
        self._power = None
        self._fuel = None
        self._wheels = None
        self.discriminator = None

        self.market = market
        self.body = body
        self.trim = trim
        self.generation = generation
        self.stud_holes = stud_holes
        self.pcd = pcd
        self.centre_bore = centre_bore
        if lock_type is not None:
            self.lock_type = lock_type
        self.lock_text = lock_text
        self.bolt_pattern = bolt_pattern
        if power is not None:
            self.power = power
        if fuel is not None:
            self.fuel = fuel
        if wheels is not None:
            self.wheels = wheels

    @property
    def market(self):
        """Gets the market of this Vehicle.  # noqa: E501


        :return: The market of this Vehicle.  # noqa: E501
        :rtype: Market
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this Vehicle.


        :param market: The market of this Vehicle.  # noqa: E501
        :type: Market
        """
        if market is None:
            raise ValueError("Invalid value for `market`, must not be `None`")  # noqa: E501

        self._market = market

    @property
    def body(self):
        """Gets the body of this Vehicle.  # noqa: E501

        Body name. Used extensively for JDM market (e.g. `GG2W`, can be __*`null`*__)  # noqa: E501

        :return: The body of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Vehicle.

        Body name. Used extensively for JDM market (e.g. `GG2W`, can be __*`null`*__)  # noqa: E501

        :param body: The body of this Vehicle.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def trim(self):
        """Gets the trim of this Vehicle.  # noqa: E501

        Trim name. It can be empty for models created for JDM market (e.g. `2.0`, can be __*`null`*__)  # noqa: E501

        :return: The trim of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._trim

    @trim.setter
    def trim(self, trim):
        """Sets the trim of this Vehicle.

        Trim name. It can be empty for models created for JDM market (e.g. `2.0`, can be __*`null`*__)  # noqa: E501

        :param trim: The trim of this Vehicle.  # noqa: E501
        :type: str
        """
        if trim is None:
            raise ValueError("Invalid value for `trim`, must not be `None`")  # noqa: E501

        self._trim = trim

    @property
    def generation(self):
        """Gets the generation of this Vehicle.  # noqa: E501


        :return: The generation of this Vehicle.  # noqa: E501
        :rtype: Generation
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this Vehicle.


        :param generation: The generation of this Vehicle.  # noqa: E501
        :type: Generation
        """
        if generation is None:
            raise ValueError("Invalid value for `generation`, must not be `None`")  # noqa: E501

        self._generation = generation

    @property
    def stud_holes(self):
        """Gets the stud_holes of this Vehicle.  # noqa: E501

        Number of stud holes (e.g. `5`, can be __*`null`*__)  # noqa: E501

        :return: The stud_holes of this Vehicle.  # noqa: E501
        :rtype: int
        """
        return self._stud_holes

    @stud_holes.setter
    def stud_holes(self, stud_holes):
        """Sets the stud_holes of this Vehicle.

        Number of stud holes (e.g. `5`, can be __*`null`*__)  # noqa: E501

        :param stud_holes: The stud_holes of this Vehicle.  # noqa: E501
        :type: int
        """
        if stud_holes is None:
            raise ValueError("Invalid value for `stud_holes`, must not be `None`")  # noqa: E501

        self._stud_holes = stud_holes

    @property
    def pcd(self):
        """Gets the pcd of this Vehicle.  # noqa: E501

        Pitch circle diameter, mm (e.g. `105`, can be __*`null`*__)  # noqa: E501

        :return: The pcd of this Vehicle.  # noqa: E501
        :rtype: float
        """
        return self._pcd

    @pcd.setter
    def pcd(self, pcd):
        """Sets the pcd of this Vehicle.

        Pitch circle diameter, mm (e.g. `105`, can be __*`null`*__)  # noqa: E501

        :param pcd: The pcd of this Vehicle.  # noqa: E501
        :type: float
        """
        if pcd is None:
            raise ValueError("Invalid value for `pcd`, must not be `None`")  # noqa: E501

        self._pcd = pcd

    @property
    def centre_bore(self):
        """Gets the centre_bore of this Vehicle.  # noqa: E501

        Centre bore diameter, mm (e.g. `48.1`, can be __*`null`*__)  # noqa: E501

        :return: The centre_bore of this Vehicle.  # noqa: E501
        :rtype: float
        """
        return self._centre_bore

    @centre_bore.setter
    def centre_bore(self, centre_bore):
        """Sets the centre_bore of this Vehicle.

        Centre bore diameter, mm (e.g. `48.1`, can be __*`null`*__)  # noqa: E501

        :param centre_bore: The centre_bore of this Vehicle.  # noqa: E501
        :type: float
        """
        if centre_bore is None:
            raise ValueError("Invalid value for `centre_bore`, must not be `None`")  # noqa: E501

        self._centre_bore = centre_bore

    @property
    def lock_type(self):
        """Gets the lock_type of this Vehicle.  # noqa: E501


        :return: The lock_type of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._lock_type

    @lock_type.setter
    def lock_type(self, lock_type):
        """Sets the lock_type of this Vehicle.


        :param lock_type: The lock_type of this Vehicle.  # noqa: E501
        :type: str
        """
        allowed_values = ["nut", "bolt"]  # noqa: E501
        if lock_type not in allowed_values:
            raise ValueError(
                "Invalid value for `lock_type` ({0}), must be one of {1}"  # noqa: E501
                .format(lock_type, allowed_values)
            )

        self._lock_type = lock_type

    @property
    def lock_text(self):
        """Gets the lock_text of this Vehicle.  # noqa: E501

        Lock thread size (e.g. `M12 x 1.25`, can be __*`null`*__)  # noqa: E501

        :return: The lock_text of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._lock_text

    @lock_text.setter
    def lock_text(self, lock_text):
        """Sets the lock_text of this Vehicle.

        Lock thread size (e.g. `M12 x 1.25`, can be __*`null`*__)  # noqa: E501

        :param lock_text: The lock_text of this Vehicle.  # noqa: E501
        :type: str
        """
        if lock_text is None:
            raise ValueError("Invalid value for `lock_text`, must not be `None`")  # noqa: E501
        allowed_values = ["M10 x 1.25", "M12 x 1.25", "M12 x 1.5", "M12 x 1.75", "M14 x 1.25", "M14 x 1.5", "M14 x 2.0", "M16 x 1.5", "3/8\" - 24 UNF", "7/16\" - 20 UNF", "1/2\" - 20 UNF", "9/16\" - 18 UNF"]  # noqa: E501
        if lock_text not in allowed_values:
            raise ValueError(
                "Invalid value for `lock_text` ({0}), must be one of {1}"  # noqa: E501
                .format(lock_text, allowed_values)
            )

        self._lock_text = lock_text

    @property
    def bolt_pattern(self):
        """Gets the bolt_pattern of this Vehicle.  # noqa: E501

        Bolt pattern (e.g. `5x105`, can be __*`N/A`*__)  # noqa: E501

        :return: The bolt_pattern of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._bolt_pattern

    @bolt_pattern.setter
    def bolt_pattern(self, bolt_pattern):
        """Sets the bolt_pattern of this Vehicle.

        Bolt pattern (e.g. `5x105`, can be __*`N/A`*__)  # noqa: E501

        :param bolt_pattern: The bolt_pattern of this Vehicle.  # noqa: E501
        :type: str
        """
        if bolt_pattern is None:
            raise ValueError("Invalid value for `bolt_pattern`, must not be `None`")  # noqa: E501

        self._bolt_pattern = bolt_pattern

    @property
    def power(self):
        """Gets the power of this Vehicle.  # noqa: E501


        :return: The power of this Vehicle.  # noqa: E501
        :rtype: Power
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this Vehicle.


        :param power: The power of this Vehicle.  # noqa: E501
        :type: Power
        """

        self._power = power

    @property
    def fuel(self):
        """Gets the fuel of this Vehicle.  # noqa: E501

        Fuel (e.g. `Petrol`, can be __*`null`*__)  # noqa: E501

        :return: The fuel of this Vehicle.  # noqa: E501
        :rtype: str
        """
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        """Sets the fuel of this Vehicle.

        Fuel (e.g. `Petrol`, can be __*`null`*__)  # noqa: E501

        :param fuel: The fuel of this Vehicle.  # noqa: E501
        :type: str
        """

        self._fuel = fuel

    @property
    def wheels(self):
        """Gets the wheels of this Vehicle.  # noqa: E501


        :return: The wheels of this Vehicle.  # noqa: E501
        :rtype: list[WheelPair]
        """
        return self._wheels

    @wheels.setter
    def wheels(self, wheels):
        """Sets the wheels of this Vehicle.


        :param wheels: The wheels of this Vehicle.  # noqa: E501
        :type: list[WheelPair]
        """

        self._wheels = wheels

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
        if not isinstance(other, Vehicle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other