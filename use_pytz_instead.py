>>> import datetime
>>> import pytz
>>> pacific = pytz.timezone('US/Pacific')
>>> eastern = pytz.timezone('US/Eastern')
>>> fmt = '%Y-%m-%d %H:%M:%S %Z%z')
  File "<stdin>", line 1
    fmt = '%Y-%m-%d %H:%M:%S %Z%z')
                                  ^
SyntaxError: invalid syntax
>>> fmt = '%Y-%m-%d %H:%M:%S %Z%z'
>>> # Year-Month-Day Hour:Minute:Second TimezoneName The offset from UTC
...
>>> utc = pytz.utc
>>> # create a shortcut to UTC time
...
>>> start = pacific.localize(datetime.datetime(2014, 4, 21, 9))
>>> # localize takes a datetime object--either naive or aware--and gives it
... # back to you with a specific timezone
...
>>> start.strftime(fmt)
'2014-04-21 09:00:00 PDT-0700'
>>> # strftime() "string-from-time" converts a datetime object to a string using
... # format parameters. In this case, we created a reusable variable that contains
... # our format parameters. Smart move.
...
>>> start_eastern = start.astimezone(eastern)
>>> start_eastern
datetime.datetime(2014, 4, 21, 12, 0, tzinfo=<DstTzInfo 'US/Eastern' EDT-1 day, 20:00:00 DST>)
>>> # why did we use astimezone() instead of localize()? localize() can work with aware timezones
... # I think... but it's really meant for assigning a timezone to a naive datetime object
... # when you've got an aware datetime object--like you have after using localize() on an obj
... # then the best course of action is to use astimezone() on the now aware object.
...
>>> start
datetime.datetime(2014, 4, 21, 9, 0, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)
>>> # Actually he just said you can't localize() an aware datetime object. Is this because
... # it will overwrite the past localization, or is it because it just won't work. Let's test.
...
>>> start = eastern.localize(datetime.datetime(2014, 4, 21, 9))
>>> start
datetime.datetime(2014, 4, 21, 9, 0, tzinfo=<DstTzInfo 'US/Eastern' EDT-1 day, 20:00:00 DST>)
>>> # Well, you can certainly overwrite the existing variable, but that probably has less to do
... # with how the localize() method works and has more to do with variables being mutable in
... # Python. Ok, next test. Go back to original start value and then try using localize on
... # start_eastern to see if the localize() method fails
...
>>> # Change of plans: see what start_eastern is now that start has changed.
...
>>> start
datetime.datetime(2014, 4, 21, 9, 0, tzinfo=<DstTzInfo 'US/Eastern' EDT-1 day, 20:00:00 DST>)
>>> start_eastern
datetime.datetime(2014, 4, 21, 12, 0, tzinfo=<DstTzInfo 'US/Eastern' EDT-1 day, 20:00:00 DST>)
>>> # Ok, so start_eastern is still three hours ahead of start, even though they're now both
... # in US/Eastern. That's really tricky, because they were supposed to be the same time
... # but once I re-loacalized start is didn't change the value of the connected start_eastern
...
>>> start = pacific.localize(datetime.datetime(2014, 4, 21, 9))
>>> start
datetime.datetime(2014, 4, 21, 9, 0, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)
>>> start_eastern
datetime.datetime(2014, 4, 21, 12, 0, tzinfo=<DstTzInfo 'US/Eastern' EDT-1 day, 20:00:00 DST>)
>>> # Ok, now I'm going to try the localize() method on a datetime object which is aware
...
>>> # start_eastern = eastern.localize....
... # turns out I don't know the syntax for throwing an existing datetime into localize
... # maybe...
...
>>> start_eastern = eastern.localize(start)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mbp/.virtualenvs/treehouse/lib/python3.4/site-packages/pytz/tzinfo.py", line 304, in localize
    raise ValueError('Not naive datetime (tzinfo is already set)')
ValueError: Not naive datetime (tzinfo is already set)
>>> # There it is... that ValueError says it all, localize won't work with an aware datetime object
...
>>> # Ok, now back to our regularly scheduled program.
...
>>> # Usually, we're going to want to work with UTC times and then only deal with timezones when
... # we're outputing the times, printing them or sending them out (to users?)
...
>>> start_utc = datetime.datetime(2014, 4, 21, 1, tzinfo=utc)
>>> start_utc
datetime.datetime(2014, 4, 21, 1, 0, tzinfo=<UTC>)
>>> start_pacific = start_utc.astimezone(pacific)
>>> start_pacific
datetime.datetime(2014, 4, 20, 18, 0, tzinfo=<DstTzInfo 'US/Pacific' PDT-1 day, 17:00:00 DST>)
>>> # If we always want to work in UTC time then we also need to know where the info we're working
... # with is coming from. If data comes in from one specific place we need to input it and translate
... # it into UTC upon import.
...
>>> auckland = pytz.timezone('Pacific/Auckland')
>>> mumbai = pytz.timezone('Asia/Calcutta')
>>> apollo_13_naive = datetime.datetime(1970, 4, 11, 14, 13)
>>> # Apollo 13 launched on April 11th, 1970 at 14:13 UTC
...
>>> apollo_13_eastern = eastern.localize(apollo_13_naive)
>>> apollo_13_naive
datetime.datetime(1970, 4, 11, 14, 13)
>>> apollo_13_eastern
datetime.datetime(1970, 4, 11, 14, 13, tzinfo=<DstTzInfo 'US/Eastern' EST-1 day, 19:00:00 STD>)
>>> # The apollo_13_eastern variable is listing the time in UTC, it just also has the conversion
... # info for translating it to EST. This is confusing. I thought that localize... oh. localize()
... # will set a tzinfo value, but it doesn't display the time in that timezone. There's a real
... # difference between setting tzinfo and showing a time in that timezone. This is a HUGE
... # difference. I've got to pay attention to this.
...
>>> # Why store values in UTC?
... # UTC doesn't have daylight savings time. So you don't need to try and remember whether the
... # original time was in daylight savings or not. You can deal with all of that when you
... # translate back to the local time.
...
>>> apollo_13_utc = apollo_13_eastern.astimezone(utc)
>>> apollo_13_utc
datetime.datetime(1970, 4, 11, 19, 13, tzinfo=<UTC>)
>>> apollo_13_utc.astimezone(pacific).strftime(fmt)
'1970-04-11 11:13:00 PST-0800'
>>> # We did two things above. First with the creation of apollo_13_utc we created an aware
... # datetime object with the tzinfo set to UTC. Second we used that variable with tzinfo set
... # to UTC to start exploring when the event happened in different timezones. That's where
... # the astimezone() method and strftime() method with our fmt string came into the equation
...
>>> apollo_13_utc.astimezone(auckland).strftime(fmt)
'1970-04-12 07:13:00 NZST+1200'
>>> apollo_13_utc.astimezone(mumbai).strftime(fmt)
'1970-04-12 00:43:00 IST+0530'
>>> pytz.all_timezones # a really convenient way to view all the timezones
['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CET', 'CST6CDT', 'Canada/Atlantic', 'Canada/Central', 'Canada/East-Saskatchewan', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT+0', 'GMT-0', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NZ', 'NZ-CHAT', 'Navajo', 'PRC', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROC', 'ROK', 'Singapore', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Pacific-New', 'US/Samoa', 'UTC', 'Universal', 'W-SU', 'WET', 'Zulu']
>>> pytz.country_timezones['us'] # a way to view just the timezones in a country, pass in a two letter code
['America/New_York', 'America/Detroit', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Indiana/Indianapolis', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Vevay', 'America/Chicago', 'America/Indiana/Tell_City', 'America/Indiana/Knox', 'America/Menominee', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/North_Dakota/Beulah', 'America/Denver', 'America/Boise', 'America/Phoenix', 'America/Los_Angeles', 'America/Metlakatla', 'America/Anchorage', 'America/Juneau', 'America/Sitka', 'America/Yakutat', 'America/Nome', 'America/Adak', 'Pacific/Honolulu']
>>>