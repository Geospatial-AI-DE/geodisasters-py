# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

from datetime import date, datetime, timedelta, timezone
from georapid.client import GeoRapidClient
from georapid.formats import OutFormat
import requests



def query(client: GeoRapidClient, from_date: date, to_date: date, format: OutFormat = OutFormat.GEOJSON):
    """
    Returns the most common locations related to natural disasters using a specific date range.
    The maximum date range is between 2023-05-24 and yesterday.

    :param client: The client instance to use for this query.
    :param from_date: The start value for the date range. Must not smaller than 2023-05-24
    :param to_date: The end value for the date range. Must not be greater than yesterday.
    :param format: Defines the output format.

    :return: The most common locations as dictionary.
    """

    if from_date < date(2023, 5, 24):
        raise ValueError(f'Invalid from_date! {from_date} is smaller than 2023-05-24.')
    
    today = datetime.now(timezone.utc).date()
    yesterday = today - timedelta(days=1)
    if yesterday < to_date:
        raise ValueError(f'Invalid to_date! {to_date} is larger than yesterday.')

    endpoint = '{0}/query'.format(client.url)
    params = {
        'from': from_date.isoformat(),
        'to': to_date.isoformat(),
        'format': str(format)
    }
    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()