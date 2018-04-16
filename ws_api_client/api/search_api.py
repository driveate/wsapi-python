# coding: utf-8

"""
    Wheel Fitment API

    The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@wheel-size.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ws_api_client.api_client import ApiClient


class SearchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def search_by_hf_tire_list(self, tire_diameter, tire_section_width, rim_diameter_hf, **kwargs):  # noqa: E501
        """Find models matching given high flotation tire  # noqa: E501

        Get a list of model modifications that match the given tire size in high flotation sizing system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_by_hf_tire_list(tire_diameter, tire_section_width, rim_diameter_hf, async=True)
        >>> result = thread.get()

        :param async bool
        :param float tire_diameter: Tire diameter, in (e.g. `31`) (required)
        :param float tire_section_width: Tire section width, in (e.g. `10.5`) (required)
        :param float rim_diameter_hf: Rim diameter, in (e.g. `15`) (required)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[MakeWithModels]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_by_hf_tire_list_with_http_info(tire_diameter, tire_section_width, rim_diameter_hf, **kwargs)  # noqa: E501
        else:
            (data) = self.search_by_hf_tire_list_with_http_info(tire_diameter, tire_section_width, rim_diameter_hf, **kwargs)  # noqa: E501
            return data

    def search_by_hf_tire_list_with_http_info(self, tire_diameter, tire_section_width, rim_diameter_hf, **kwargs):  # noqa: E501
        """Find models matching given high flotation tire  # noqa: E501

        Get a list of model modifications that match the given tire size in high flotation sizing system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_by_hf_tire_list_with_http_info(tire_diameter, tire_section_width, rim_diameter_hf, async=True)
        >>> result = thread.get()

        :param async bool
        :param float tire_diameter: Tire diameter, in (e.g. `31`) (required)
        :param float tire_section_width: Tire section width, in (e.g. `10.5`) (required)
        :param float rim_diameter_hf: Rim diameter, in (e.g. `15`) (required)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[MakeWithModels]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tire_diameter', 'tire_section_width', 'rim_diameter_hf', 'lang', 'brands', 'brands_exclude', 'countries', 'countries_exclude']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_by_hf_tire_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tire_diameter' is set
        if ('tire_diameter' not in params or
                params['tire_diameter'] is None):
            raise ValueError("Missing the required parameter `tire_diameter` when calling `search_by_hf_tire_list`")  # noqa: E501
        # verify the required parameter 'tire_section_width' is set
        if ('tire_section_width' not in params or
                params['tire_section_width'] is None):
            raise ValueError("Missing the required parameter `tire_section_width` when calling `search_by_hf_tire_list`")  # noqa: E501
        # verify the required parameter 'rim_diameter_hf' is set
        if ('rim_diameter_hf' not in params or
                params['rim_diameter_hf'] is None):
            raise ValueError("Missing the required parameter `rim_diameter_hf` when calling `search_by_hf_tire_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tire_diameter' in params:
            query_params.append(('tire_diameter', params['tire_diameter']))  # noqa: E501
        if 'tire_section_width' in params:
            query_params.append(('tire_section_width', params['tire_section_width']))  # noqa: E501
        if 'rim_diameter_hf' in params:
            query_params.append(('rim_diameter_hf', params['rim_diameter_hf']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'brands' in params:
            query_params.append(('brands', params['brands']))  # noqa: E501
        if 'brands_exclude' in params:
            query_params.append(('brands_exclude', params['brands_exclude']))  # noqa: E501
        if 'countries' in params:
            query_params.append(('countries', params['countries']))  # noqa: E501
        if 'countries_exclude' in params:
            query_params.append(('countries_exclude', params['countries_exclude']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user_key']  # noqa: E501

        return self.api_client.call_api(
            '/search/by_hf_tire/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MakeWithModels]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_by_model_list(self, make, model, year, **kwargs):  # noqa: E501
        """Find OE and option fitments by model/year/trim  # noqa: E501

        Find OE and option fitments that match the given manufacturer, model, year and trim.  **It's an alias** for _**`GET /vehicles/`**_ method  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_by_model_list(make, model, year, async=True)
        >>> result = thread.get()

        :param async bool
        :param str make: Manufacturer slug name, use _**`GET /makes/`**_ to get possible values (e.g. `mitsubishi`) (required)
        :param str model: Model slug name, use _**`GET /models/`**_ to get possible values (e.g. `outlander`) (required)
        :param int year: You can use _**`GET /years/`**_ to get possible years (e.g. `2015`) (required)
        :param str trim: Use *`slug`* from _**`GET /trims/`**_ methods here. (e.g. `2.0+GG2W`)
        :param bool only_oem: Show only original equipment wheels
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
        :return: list[Vehicle]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_by_model_list_with_http_info(make, model, year, **kwargs)  # noqa: E501
        else:
            (data) = self.search_by_model_list_with_http_info(make, model, year, **kwargs)  # noqa: E501
            return data

    def search_by_model_list_with_http_info(self, make, model, year, **kwargs):  # noqa: E501
        """Find OE and option fitments by model/year/trim  # noqa: E501

        Find OE and option fitments that match the given manufacturer, model, year and trim.  **It's an alias** for _**`GET /vehicles/`**_ method  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_by_model_list_with_http_info(make, model, year, async=True)
        >>> result = thread.get()

        :param async bool
        :param str make: Manufacturer slug name, use _**`GET /makes/`**_ to get possible values (e.g. `mitsubishi`) (required)
        :param str model: Model slug name, use _**`GET /models/`**_ to get possible values (e.g. `outlander`) (required)
        :param int year: You can use _**`GET /years/`**_ to get possible years (e.g. `2015`) (required)
        :param str trim: Use *`slug`* from _**`GET /trims/`**_ methods here. (e.g. `2.0+GG2W`)
        :param bool only_oem: Show only original equipment wheels
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
        :return: list[Vehicle]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['make', 'model', 'year', 'trim', 'only_oem', 'lang']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_by_model_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'make' is set
        if ('make' not in params or
                params['make'] is None):
            raise ValueError("Missing the required parameter `make` when calling `search_by_model_list`")  # noqa: E501
        # verify the required parameter 'model' is set
        if ('model' not in params or
                params['model'] is None):
            raise ValueError("Missing the required parameter `model` when calling `search_by_model_list`")  # noqa: E501
        # verify the required parameter 'year' is set
        if ('year' not in params or
                params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `search_by_model_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'make' in params:
            query_params.append(('make', params['make']))  # noqa: E501
        if 'model' in params:
            query_params.append(('model', params['model']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'trim' in params:
            query_params.append(('trim', params['trim']))  # noqa: E501
        if 'only_oem' in params:
            query_params.append(('only_oem', params['only_oem']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user_key']  # noqa: E501

        return self.api_client.call_api(
            '/search/by_model/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Vehicle]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_by_rim_list(self, bolt_pattern, rim_diameter, rim_width, **kwargs):  # noqa: E501
        """Find models matching given rim parameters  # noqa: E501

        Get a list of model modifications that match the given rim parameters, grouped by manufacturer.  It's an alias for _**`GET /bolt-patterns/{bolt_pattern}/`**_        method with given path and query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_by_rim_list(bolt_pattern, rim_diameter, rim_width, async=True)
        >>> result = thread.get()

        :param async bool
        :param str bolt_pattern: Bolt pattern combines number of stud holes and pitch circle diameter. Use _**`GET /bolt-patterns/`**_ to get possible values (e.g. `5x105`) (required)
        :param float rim_diameter: Rim diameter, in (e.g. `16`) (required)
        :param float rim_width: Rim width, in (e.g. `7`) (required)
        :param float offset: Rim offset, mm (e.g. `40`)
        :param float offset_min: Lower bound for rim offset, mm (e.g. `35`)
        :param float offset_max: Upper bound for rim offset, mm (e.g. `45`)
        :param float cb: Centre bore value, mm (e.g. `60`)
        :param float cb_min: Lower bound for centre bore value, mm (e.g. `55`)
        :param float cb_max: Upper bound for centre bore value, mm (e.g. `65`)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[MakeWithModels]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_by_rim_list_with_http_info(bolt_pattern, rim_diameter, rim_width, **kwargs)  # noqa: E501
        else:
            (data) = self.search_by_rim_list_with_http_info(bolt_pattern, rim_diameter, rim_width, **kwargs)  # noqa: E501
            return data

    def search_by_rim_list_with_http_info(self, bolt_pattern, rim_diameter, rim_width, **kwargs):  # noqa: E501
        """Find models matching given rim parameters  # noqa: E501

        Get a list of model modifications that match the given rim parameters, grouped by manufacturer.  It's an alias for _**`GET /bolt-patterns/{bolt_pattern}/`**_        method with given path and query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_by_rim_list_with_http_info(bolt_pattern, rim_diameter, rim_width, async=True)
        >>> result = thread.get()

        :param async bool
        :param str bolt_pattern: Bolt pattern combines number of stud holes and pitch circle diameter. Use _**`GET /bolt-patterns/`**_ to get possible values (e.g. `5x105`) (required)
        :param float rim_diameter: Rim diameter, in (e.g. `16`) (required)
        :param float rim_width: Rim width, in (e.g. `7`) (required)
        :param float offset: Rim offset, mm (e.g. `40`)
        :param float offset_min: Lower bound for rim offset, mm (e.g. `35`)
        :param float offset_max: Upper bound for rim offset, mm (e.g. `45`)
        :param float cb: Centre bore value, mm (e.g. `60`)
        :param float cb_min: Lower bound for centre bore value, mm (e.g. `55`)
        :param float cb_max: Upper bound for centre bore value, mm (e.g. `65`)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[MakeWithModels]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bolt_pattern', 'rim_diameter', 'rim_width', 'offset', 'offset_min', 'offset_max', 'cb', 'cb_min', 'cb_max', 'lang', 'brands', 'brands_exclude', 'countries', 'countries_exclude']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_by_rim_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bolt_pattern' is set
        if ('bolt_pattern' not in params or
                params['bolt_pattern'] is None):
            raise ValueError("Missing the required parameter `bolt_pattern` when calling `search_by_rim_list`")  # noqa: E501
        # verify the required parameter 'rim_diameter' is set
        if ('rim_diameter' not in params or
                params['rim_diameter'] is None):
            raise ValueError("Missing the required parameter `rim_diameter` when calling `search_by_rim_list`")  # noqa: E501
        # verify the required parameter 'rim_width' is set
        if ('rim_width' not in params or
                params['rim_width'] is None):
            raise ValueError("Missing the required parameter `rim_width` when calling `search_by_rim_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'bolt_pattern' in params:
            query_params.append(('bolt_pattern', params['bolt_pattern']))  # noqa: E501
        if 'rim_diameter' in params:
            query_params.append(('rim_diameter', params['rim_diameter']))  # noqa: E501
        if 'rim_width' in params:
            query_params.append(('rim_width', params['rim_width']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'offset_min' in params:
            query_params.append(('offset_min', params['offset_min']))  # noqa: E501
        if 'offset_max' in params:
            query_params.append(('offset_max', params['offset_max']))  # noqa: E501
        if 'cb' in params:
            query_params.append(('cb', params['cb']))  # noqa: E501
        if 'cb_min' in params:
            query_params.append(('cb_min', params['cb_min']))  # noqa: E501
        if 'cb_max' in params:
            query_params.append(('cb_max', params['cb_max']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'brands' in params:
            query_params.append(('brands', params['brands']))  # noqa: E501
        if 'brands_exclude' in params:
            query_params.append(('brands_exclude', params['brands_exclude']))  # noqa: E501
        if 'countries' in params:
            query_params.append(('countries', params['countries']))  # noqa: E501
        if 'countries_exclude' in params:
            query_params.append(('countries_exclude', params['countries_exclude']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user_key']  # noqa: E501

        return self.api_client.call_api(
            '/search/by_rim/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MakeWithModels]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_by_tire_list(self, tire_width, aspect_ratio, rim_diameter, **kwargs):  # noqa: E501
        """Find models matching given tire parameters  # noqa: E501

        Get a list of model modifications matching given tire, grouped by manufacturer.  It's an alias for _**`GET /tire/{tire}/`**_ method  (tire configuration is combined of required tire width, aspect ratio and rim diameter).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_by_tire_list(tire_width, aspect_ratio, rim_diameter, async=True)
        >>> result = thread.get()

        :param async bool
        :param float tire_width: Tire width, mm (e.g. `195`) (required)
        :param float aspect_ratio: Aspect ratio, % (e.g. `50`) (required)
        :param float rim_diameter: Rim diameter, in (e.g. `16`) (required)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[MakeWithModels]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.search_by_tire_list_with_http_info(tire_width, aspect_ratio, rim_diameter, **kwargs)  # noqa: E501
        else:
            (data) = self.search_by_tire_list_with_http_info(tire_width, aspect_ratio, rim_diameter, **kwargs)  # noqa: E501
            return data

    def search_by_tire_list_with_http_info(self, tire_width, aspect_ratio, rim_diameter, **kwargs):  # noqa: E501
        """Find models matching given tire parameters  # noqa: E501

        Get a list of model modifications matching given tire, grouped by manufacturer.  It's an alias for _**`GET /tire/{tire}/`**_ method  (tire configuration is combined of required tire width, aspect ratio and rim diameter).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.search_by_tire_list_with_http_info(tire_width, aspect_ratio, rim_diameter, async=True)
        >>> result = thread.get()

        :param async bool
        :param float tire_width: Tire width, mm (e.g. `195`) (required)
        :param float aspect_ratio: Aspect ratio, % (e.g. `50`) (required)
        :param float rim_diameter: Rim diameter, in (e.g. `16`) (required)
        :param str lang: Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only
        :param str brands: Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`)
        :param str brands_exclude: Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`)
        :param str countries: Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`)
        :param str countries_exclude: Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`)
        :return: list[MakeWithModels]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tire_width', 'aspect_ratio', 'rim_diameter', 'lang', 'brands', 'brands_exclude', 'countries', 'countries_exclude']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_by_tire_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tire_width' is set
        if ('tire_width' not in params or
                params['tire_width'] is None):
            raise ValueError("Missing the required parameter `tire_width` when calling `search_by_tire_list`")  # noqa: E501
        # verify the required parameter 'aspect_ratio' is set
        if ('aspect_ratio' not in params or
                params['aspect_ratio'] is None):
            raise ValueError("Missing the required parameter `aspect_ratio` when calling `search_by_tire_list`")  # noqa: E501
        # verify the required parameter 'rim_diameter' is set
        if ('rim_diameter' not in params or
                params['rim_diameter'] is None):
            raise ValueError("Missing the required parameter `rim_diameter` when calling `search_by_tire_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tire_width' in params:
            query_params.append(('tire_width', params['tire_width']))  # noqa: E501
        if 'aspect_ratio' in params:
            query_params.append(('aspect_ratio', params['aspect_ratio']))  # noqa: E501
        if 'rim_diameter' in params:
            query_params.append(('rim_diameter', params['rim_diameter']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501
        if 'brands' in params:
            query_params.append(('brands', params['brands']))  # noqa: E501
        if 'brands_exclude' in params:
            query_params.append(('brands_exclude', params['brands_exclude']))  # noqa: E501
        if 'countries' in params:
            query_params.append(('countries', params['countries']))  # noqa: E501
        if 'countries_exclude' in params:
            query_params.append(('countries_exclude', params['countries_exclude']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['user_key']  # noqa: E501

        return self.api_client.call_api(
            '/search/by_tire/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MakeWithModels]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)