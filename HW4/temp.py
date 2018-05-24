#api_url = "https://api.forecast.io/forecast/9a88eacea38fe5789edcc1687a9921d7/{},{}"

# https://github.com/tdlm/fun-with-python/blob/master/states_and_capitals.py
# https://www.jetpunk.com/data/countries/united-states/state-capitals-list
'''states = {
        'AL':{'lat': 32.3617, 'long': -86.2792},
        'AK':{'lat': 58.3014, 'long': -134.4220},
        'AZ':{'lat': 33.4500, 'long': -112.0670},
        'AR':{'lat': 34.7361, 'long': -92.3311},
        'CA':{'lat': 38.5556, 'long': -121.4690},
        'CO':{'lat': 39.7618, 'long': -104.8810},
        'CT':{'lat': 41.7627, 'long': -72.6743},
        'DE':{'lat': 39.1619, 'long': -75.5267},
        'FL':{'lat': 30.4550, 'long': -84.2533},
        'GA':{'lat': 33.7550, 'long': -84.3900},
        'HI':{'lat': 21.3000, 'long': -157.8170},
        'ID':{'lat': 43.6167, 'long': -116.2000},
        'IL':{'lat': 39.6983, 'long': -89.6197},
        'IN':{'lat': 39.7910, 'long': -86.1480},
        'IA':{'lat': 41.5908, 'long': -93.6208},
        'KS':{'lat': 39.0558, 'long': -95.6894},
        'KY':{'lat': 38.1970, 'long': -84.8630},
        'LA':{'lat': 30.4500, 'long': -91.1400},
        'ME':{'lat': 44.3070, 'long': -69.7820},
        'MD':{'lat': 38.9729, 'long': -76.5012},
        'MA':{'lat': 42.3581, 'long': -71.0636},
        'MI':{'lat': 42.7336, 'long': -84.5467},
        'MN':{'lat': 44.9442, 'long': -93.0936},
        'MS':{'lat': 32.2989, 'long': -90.1847},
        'MO':{'lat': 38.5767, 'long': -92.1736},
        'MT':{'lat': 46.5958, 'long': -112.0270},
        'NE':{'lat': 40.8106, 'long': -96.6803},
        'NV':{'lat': 39.1608, 'long': -119.7540},
        'NH':{'lat': 43.2067, 'long': -71.5381},
        'NJ':{'lat': 40.2237, 'long': -74.7640},
        'NM':{'lat': 35.6672, 'long': -105.9640},
        'NY':{'lat': 42.6525, 'long': -73.7572},
        'NC':{'lat': 35.7667, 'long': -78.6333},
        'ND':{'lat': 46.8133, 'long': -100.7790},
        'OH':{'lat': 39.9833, 'long': -82.9833},
        'OK':{'lat': 35.4822, 'long': -97.5350},
        'OR':{'lat': 44.9308, 'long': -123.0290},
        'PA':{'lat': 40.2697, 'long': -76.8756},
        'RI':{'lat': 41.8236, 'long': -71.4222},
        'SC':{'lat': 34.0006, 'long': -81.0347},
        'SD':{'lat': 44.3680, 'long': -100.3360},
        'TN':{'lat': 36.1667, 'long': -86.7833},
        'TX':{'lat': 30.2500, 'long': -97.7500},
        'UT':{'lat': 40.7500, 'long': -111.8830},
        'VT':{'lat': 44.2597, 'long': -72.5750},
        'VA':{'lat': 37.5333, 'long': -77.4667},
        'WA':{'lat': 47.0425, 'long': -122.8930},
        'WV':{'lat': 38.3472, 'long': -81.6333},
        'WI':{'lat': 43.0667, 'long': -89.4000},
        'WY':{'lat': 41.1456, 'long': -104.8020}
    }
'''


'''
  # print(response)

  print """
    <script>
    $( document ).ready(function() {
  """

  for code, coords in states.items():
    # Make API call and get data
    # https://stackoverflow.com/a/35120519/5055644
    r = requests.get(url=api_url.format(coords['lat'], coords['long']))
    response = r.json()
    temp = response['currently']['temperature']

    # Get color
    if temp <= 10:
        color = "blue"
    elif temp <= 30:
        color = "cyan"
    elif temp <= 50:
        color = "green"
    elif temp <= 80:
        color = "orange"
    else:
        color = "red"
    
    print "$('#{}').css('fill', '{}');".format(code, color)

  print """
    });
    </script>
  """

  print("""</body></html>""")
'''