# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import core.models.instance
import core.models.network
import core.models.serviceclass
import encrypted_fields.fields
import geoposition.fields
import timezones.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255,
                                            verbose_name=b'email address', db_index=True)),
                ('username', models.CharField(default=b'Something', max_length=255)),
                ('firstname', models.CharField(
                    help_text=b"person's given name", max_length=200)),
                ('lastname', models.CharField(
                    help_text=b"person's surname", max_length=200)),
                ('phone', models.CharField(help_text=b'phone number contact',
                                           max_length=100, null=True, blank=True)),
                ('user_url', models.URLField(null=True, blank=True)),
                ('public_key', models.TextField(
                    help_text=b'Public key string', max_length=1024, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_readonly', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('enacted', models.DateTimeField(default=None, null=True)),
                ('policed', models.DateTimeField(default=None, null=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('timezone', timezones.fields.TimeZoneField(default=b'America/New_York', max_length=100, choices=[(b'Pacific/Midway', b'(GMT-1100) Pacific/Midway'), (b'Pacific/Niue', b'(GMT-1100) Pacific/Niue'), (b'Pacific/Pago_Pago', b'(GMT-1100) Pacific/Pago_Pago'), (b'America/Adak', b'(GMT-1000) America/Adak'), (b'Pacific/Honolulu', b'(GMT-1000) Pacific/Honolulu'), (b'Pacific/Johnston', b'(GMT-1000) Pacific/Johnston'), (b'Pacific/Rarotonga', b'(GMT-1000) Pacific/Rarotonga'), (b'Pacific/Tahiti', b'(GMT-1000) Pacific/Tahiti'), (b'US/Hawaii', b'(GMT-1000) US/Hawaii'), (b'Pacific/Marquesas', b'(GMT-0930) Pacific/Marquesas'), (b'America/Anchorage', b'(GMT-0900) America/Anchorage'), (b'America/Juneau', b'(GMT-0900) America/Juneau'), (b'America/Nome', b'(GMT-0900) America/Nome'), (b'America/Sitka', b'(GMT-0900) America/Sitka'), (b'America/Yakutat', b'(GMT-0900) America/Yakutat'), (b'Pacific/Gambier', b'(GMT-0900) Pacific/Gambier'), (b'US/Alaska', b'(GMT-0900) US/Alaska'), (b'America/Dawson', b'(GMT-0800) America/Dawson'), (b'America/Los_Angeles', b'(GMT-0800) America/Los_Angeles'), (b'America/Metlakatla', b'(GMT-0800) America/Metlakatla'), (b'America/Santa_Isabel', b'(GMT-0800) America/Santa_Isabel'), (b'America/Tijuana', b'(GMT-0800) America/Tijuana'), (b'America/Vancouver', b'(GMT-0800) America/Vancouver'), (b'America/Whitehorse', b'(GMT-0800) America/Whitehorse'), (b'Canada/Pacific', b'(GMT-0800) Canada/Pacific'), (b'Pacific/Pitcairn', b'(GMT-0800) Pacific/Pitcairn'), (b'US/Pacific', b'(GMT-0800) US/Pacific'), (b'America/Boise', b'(GMT-0700) America/Boise'), (b'America/Cambridge_Bay', b'(GMT-0700) America/Cambridge_Bay'), (b'America/Chihuahua', b'(GMT-0700) America/Chihuahua'), (b'America/Creston', b'(GMT-0700) America/Creston'), (b'America/Dawson_Creek', b'(GMT-0700) America/Dawson_Creek'), (b'America/Denver', b'(GMT-0700) America/Denver'), (b'America/Edmonton', b'(GMT-0700) America/Edmonton'), (b'America/Hermosillo', b'(GMT-0700) America/Hermosillo'), (b'America/Inuvik', b'(GMT-0700) America/Inuvik'), (b'America/Mazatlan', b'(GMT-0700) America/Mazatlan'), (b'America/Ojinaga', b'(GMT-0700) America/Ojinaga'), (b'America/Phoenix', b'(GMT-0700) America/Phoenix'), (b'America/Shiprock', b'(GMT-0700) America/Shiprock'), (b'America/Yellowknife', b'(GMT-0700) America/Yellowknife'), (b'Canada/Mountain', b'(GMT-0700) Canada/Mountain'), (b'US/Arizona', b'(GMT-0700) US/Arizona'), (b'US/Mountain', b'(GMT-0700) US/Mountain'), (b'America/Bahia_Banderas', b'(GMT-0600) America/Bahia_Banderas'), (b'America/Belize', b'(GMT-0600) America/Belize'), (b'America/Cancun', b'(GMT-0600) America/Cancun'), (b'America/Chicago', b'(GMT-0600) America/Chicago'), (b'America/Costa_Rica', b'(GMT-0600) America/Costa_Rica'), (b'America/El_Salvador', b'(GMT-0600) America/El_Salvador'), (b'America/Guatemala', b'(GMT-0600) America/Guatemala'), (b'America/Indiana/Knox', b'(GMT-0600) America/Indiana/Knox'), (b'America/Indiana/Tell_City', b'(GMT-0600) America/Indiana/Tell_City'), (b'America/Managua', b'(GMT-0600) America/Managua'), (b'America/Matamoros', b'(GMT-0600) America/Matamoros'), (b'America/Menominee', b'(GMT-0600) America/Menominee'), (b'America/Merida', b'(GMT-0600) America/Merida'), (b'America/Mexico_City', b'(GMT-0600) America/Mexico_City'), (b'America/Monterrey', b'(GMT-0600) America/Monterrey'), (b'America/North_Dakota/Beulah', b'(GMT-0600) America/North_Dakota/Beulah'), (b'America/North_Dakota/Center', b'(GMT-0600) America/North_Dakota/Center'), (b'America/North_Dakota/New_Salem', b'(GMT-0600) America/North_Dakota/New_Salem'), (b'America/Rainy_River', b'(GMT-0600) America/Rainy_River'), (b'America/Rankin_Inlet', b'(GMT-0600) America/Rankin_Inlet'), (b'America/Regina', b'(GMT-0600) America/Regina'), (b'America/Resolute', b'(GMT-0600) America/Resolute'), (b'America/Swift_Current', b'(GMT-0600) America/Swift_Current'), (b'America/Tegucigalpa', b'(GMT-0600) America/Tegucigalpa'), (b'America/Winnipeg', b'(GMT-0600) America/Winnipeg'), (b'Canada/Central', b'(GMT-0600) Canada/Central'), (b'Pacific/Galapagos', b'(GMT-0600) Pacific/Galapagos'), (b'US/Central', b'(GMT-0600) US/Central'), (b'America/Atikokan', b'(GMT-0500) America/Atikokan'), (b'America/Bogota', b'(GMT-0500) America/Bogota'), (b'America/Cayman', b'(GMT-0500) America/Cayman'), (b'America/Detroit', b'(GMT-0500) America/Detroit'), (b'America/Eirunepe', b'(GMT-0500) America/Eirunepe'), (b'America/Grand_Turk', b'(GMT-0500) America/Grand_Turk'), (b'America/Guayaquil', b'(GMT-0500) America/Guayaquil'), (b'America/Havana', b'(GMT-0500) America/Havana'), (b'America/Indiana/Indianapolis', b'(GMT-0500) America/Indiana/Indianapolis'), (b'America/Indiana/Marengo', b'(GMT-0500) America/Indiana/Marengo'), (b'America/Indiana/Petersburg', b'(GMT-0500) America/Indiana/Petersburg'), (b'America/Indiana/Vevay', b'(GMT-0500) America/Indiana/Vevay'), (b'America/Indiana/Vincennes', b'(GMT-0500) America/Indiana/Vincennes'), (b'America/Indiana/Winamac', b'(GMT-0500) America/Indiana/Winamac'), (b'America/Iqaluit', b'(GMT-0500) America/Iqaluit'), (b'America/Jamaica', b'(GMT-0500) America/Jamaica'), (b'America/Kentucky/Louisville', b'(GMT-0500) America/Kentucky/Louisville'), (b'America/Kentucky/Monticello', b'(GMT-0500) America/Kentucky/Monticello'), (b'America/Lima', b'(GMT-0500) America/Lima'), (b'America/Montreal', b'(GMT-0500) America/Montreal'), (b'America/Nassau', b'(GMT-0500) America/Nassau'), (b'America/New_York', b'(GMT-0500) America/New_York'), (b'America/Nipigon', b'(GMT-0500) America/Nipigon'), (b'America/Panama', b'(GMT-0500) America/Panama'), (b'America/Pangnirtung', b'(GMT-0500) America/Pangnirtung'), (b'America/Port-au-Prince', b'(GMT-0500) America/Port-au-Prince'), (b'America/Rio_Branco', b'(GMT-0500) America/Rio_Branco'), (b'America/Thunder_Bay', b'(GMT-0500) America/Thunder_Bay'), (b'America/Toronto', b'(GMT-0500) America/Toronto'), (b'Canada/Eastern', b'(GMT-0500) Canada/Eastern'), (b'Pacific/Easter', b'(GMT-0500) Pacific/Easter'), (b'US/Eastern', b'(GMT-0500) US/Eastern'), (b'America/Caracas', b'(GMT-0430) America/Caracas'), (b'America/Anguilla', b'(GMT-0400) America/Anguilla'), (b'America/Antigua', b'(GMT-0400) America/Antigua'), (b'America/Aruba', b'(GMT-0400) America/Aruba'), (b'America/Barbados', b'(GMT-0400) America/Barbados'), (b'America/Blanc-Sablon', b'(GMT-0400) America/Blanc-Sablon'), (b'America/Boa_Vista', b'(GMT-0400) America/Boa_Vista'), (b'America/Curacao', b'(GMT-0400) America/Curacao'), (b'America/Dominica', b'(GMT-0400) America/Dominica'), (b'America/Glace_Bay', b'(GMT-0400) America/Glace_Bay'), (b'America/Goose_Bay', b'(GMT-0400) America/Goose_Bay'), (b'America/Grenada', b'(GMT-0400) America/Grenada'), (b'America/Guadeloupe', b'(GMT-0400) America/Guadeloupe'), (b'America/Guyana', b'(GMT-0400) America/Guyana'), (b'America/Halifax', b'(GMT-0400) America/Halifax'), (b'America/Kralendijk', b'(GMT-0400) America/Kralendijk'), (b'America/La_Paz', b'(GMT-0400) America/La_Paz'), (b'America/Lower_Princes', b'(GMT-0400) America/Lower_Princes'), (b'America/Manaus', b'(GMT-0400) America/Manaus'), (b'America/Marigot', b'(GMT-0400) America/Marigot'), (b'America/Martinique', b'(GMT-0400) America/Martinique'), (b'America/Moncton', b'(GMT-0400) America/Moncton'), (b'America/Montserrat', b'(GMT-0400) America/Montserrat'), (b'America/Port_of_Spain', b'(GMT-0400) America/Port_of_Spain'), (b'America/Porto_Velho', b'(GMT-0400) America/Porto_Velho'), (b'America/Puerto_Rico', b'(GMT-0400) America/Puerto_Rico'), (b'America/Santo_Domingo', b'(GMT-0400) America/Santo_Domingo'), (b'America/St_Barthelemy', b'(GMT-0400) America/St_Barthelemy'), (b'America/St_Kitts', b'(GMT-0400) America/St_Kitts'), (b'America/St_Lucia', b'(GMT-0400) America/St_Lucia'), (b'America/St_Thomas', b'(GMT-0400) America/St_Thomas'), (b'America/St_Vincent', b'(GMT-0400) America/St_Vincent'), (b'America/Thule', b'(GMT-0400) America/Thule'), (b'America/Tortola', b'(GMT-0400) America/Tortola'), (b'Atlantic/Bermuda', b'(GMT-0400) Atlantic/Bermuda'), (b'Canada/Atlantic', b'(GMT-0400) Canada/Atlantic'), (b'America/St_Johns', b'(GMT-0330) America/St_Johns'), (b'Canada/Newfoundland', b'(GMT-0330) Canada/Newfoundland'), (b'America/Araguaina', b'(GMT-0300) America/Araguaina'), (b'America/Argentina/Buenos_Aires', b'(GMT-0300) America/Argentina/Buenos_Aires'), (b'America/Argentina/Catamarca', b'(GMT-0300) America/Argentina/Catamarca'), (b'America/Argentina/Cordoba', b'(GMT-0300) America/Argentina/Cordoba'), (b'America/Argentina/Jujuy', b'(GMT-0300) America/Argentina/Jujuy'), (b'America/Argentina/La_Rioja', b'(GMT-0300) America/Argentina/La_Rioja'), (b'America/Argentina/Mendoza', b'(GMT-0300) America/Argentina/Mendoza'), (b'America/Argentina/Rio_Gallegos', b'(GMT-0300) America/Argentina/Rio_Gallegos'), (b'America/Argentina/Salta', b'(GMT-0300) America/Argentina/Salta'), (b'America/Argentina/San_Juan', b'(GMT-0300) America/Argentina/San_Juan'), (b'America/Argentina/San_Luis', b'(GMT-0300) America/Argentina/San_Luis'), (b'America/Argentina/Tucuman', b'(GMT-0300) America/Argentina/Tucuman'), (b'America/Argentina/Ushuaia', b'(GMT-0300) America/Argentina/Ushuaia'), (b'America/Asuncion', b'(GMT-0300) America/Asuncion'), (b'America/Bahia', b'(GMT-0300) America/Bahia'), (b'America/Belem', b'(GMT-0300) America/Belem'), (b'America/Campo_Grande', b'(GMT-0300) America/Campo_Grande'), (b'America/Cayenne', b'(GMT-0300) America/Cayenne'), (b'America/Cuiaba', b'(GMT-0300) America/Cuiaba'), (b'America/Fortaleza', b'(GMT-0300) America/Fortaleza'), (b'America/Godthab', b'(GMT-0300) America/Godthab'), (b'America/Maceio', b'(GMT-0300) America/Maceio'), (b'America/Miquelon', b'(GMT-0300) America/Miquelon'), (b'America/Paramaribo', b'(GMT-0300) America/Paramaribo'), (b'America/Recife', b'(GMT-0300) America/Recife'), (b'America/Santarem', b'(GMT-0300) America/Santarem'), (b'America/Santiago', b'(GMT-0300) America/Santiago'), (b'Antarctica/Palmer', b'(GMT-0300) Antarctica/Palmer'), (b'Antarctica/Rothera', b'(GMT-0300) Antarctica/Rothera'), (b'Atlantic/Stanley', b'(GMT-0300) Atlantic/Stanley'), (b'America/Montevideo', b'(GMT-0200) America/Montevideo'), (b'America/Noronha', b'(GMT-0200) America/Noronha'), (b'America/Sao_Paulo', b'(GMT-0200) America/Sao_Paulo'), (b'Atlantic/South_Georgia', b'(GMT-0200) Atlantic/South_Georgia'), (b'America/Scoresbysund', b'(GMT-0100) America/Scoresbysund'), (b'Atlantic/Azores', b'(GMT-0100) Atlantic/Azores'), (b'Atlantic/Cape_Verde', b'(GMT-0100) Atlantic/Cape_Verde'), (b'Africa/Abidjan', b'(GMT+0000) Africa/Abidjan'), (b'Africa/Accra', b'(GMT+0000) Africa/Accra'), (b'Africa/Bamako', b'(GMT+0000) Africa/Bamako'), (b'Africa/Banjul', b'(GMT+0000) Africa/Banjul'), (b'Africa/Bissau', b'(GMT+0000) Africa/Bissau'), (b'Africa/Casablanca', b'(GMT+0000) Africa/Casablanca'), (b'Africa/Conakry', b'(GMT+0000) Africa/Conakry'), (b'Africa/Dakar', b'(GMT+0000) Africa/Dakar'), (b'Africa/El_Aaiun', b'(GMT+0000) Africa/El_Aaiun'), (b'Africa/Freetown', b'(GMT+0000) Africa/Freetown'), (b'Africa/Lome', b'(GMT+0000) Africa/Lome'), (b'Africa/Monrovia', b'(GMT+0000) Africa/Monrovia'), (b'Africa/Nouakchott', b'(GMT+0000) Africa/Nouakchott'), (b'Africa/Ouagadougou', b'(GMT+0000) Africa/Ouagadougou'), (b'Africa/Sao_Tome', b'(GMT+0000) Africa/Sao_Tome'), (b'America/Danmarkshavn', b'(GMT+0000) America/Danmarkshavn'), (b'Atlantic/Canary', b'(GMT+0000) Atlantic/Canary'), (b'Atlantic/Faroe', b'(GMT+0000) Atlantic/Faroe'), (b'Atlantic/Madeira', b'(GMT+0000) Atlantic/Madeira'), (b'Atlantic/Reykjavik', b'(GMT+0000) Atlantic/Reykjavik'), (b'Atlantic/St_Helena', b'(GMT+0000) Atlantic/St_Helena'), (b'Europe/Dublin', b'(GMT+0000) Europe/Dublin'), (b'Europe/Guernsey', b'(GMT+0000) Europe/Guernsey'), (
                    b'Europe/Isle_of_Man', b'(GMT+0000) Europe/Isle_of_Man'), (b'Europe/Jersey', b'(GMT+0000) Europe/Jersey'), (b'Europe/Lisbon', b'(GMT+0000) Europe/Lisbon'), (b'Europe/London', b'(GMT+0000) Europe/London'), (b'GMT', b'(GMT+0000) GMT'), (b'UTC', b'(GMT+0000) UTC'), (b'Africa/Algiers', b'(GMT+0100) Africa/Algiers'), (b'Africa/Bangui', b'(GMT+0100) Africa/Bangui'), (b'Africa/Brazzaville', b'(GMT+0100) Africa/Brazzaville'), (b'Africa/Ceuta', b'(GMT+0100) Africa/Ceuta'), (b'Africa/Douala', b'(GMT+0100) Africa/Douala'), (b'Africa/Kinshasa', b'(GMT+0100) Africa/Kinshasa'), (b'Africa/Lagos', b'(GMT+0100) Africa/Lagos'), (b'Africa/Libreville', b'(GMT+0100) Africa/Libreville'), (b'Africa/Luanda', b'(GMT+0100) Africa/Luanda'), (b'Africa/Malabo', b'(GMT+0100) Africa/Malabo'), (b'Africa/Ndjamena', b'(GMT+0100) Africa/Ndjamena'), (b'Africa/Niamey', b'(GMT+0100) Africa/Niamey'), (b'Africa/Porto-Novo', b'(GMT+0100) Africa/Porto-Novo'), (b'Africa/Tunis', b'(GMT+0100) Africa/Tunis'), (b'Arctic/Longyearbyen', b'(GMT+0100) Arctic/Longyearbyen'), (b'Europe/Amsterdam', b'(GMT+0100) Europe/Amsterdam'), (b'Europe/Andorra', b'(GMT+0100) Europe/Andorra'), (b'Europe/Belgrade', b'(GMT+0100) Europe/Belgrade'), (b'Europe/Berlin', b'(GMT+0100) Europe/Berlin'), (b'Europe/Bratislava', b'(GMT+0100) Europe/Bratislava'), (b'Europe/Brussels', b'(GMT+0100) Europe/Brussels'), (b'Europe/Budapest', b'(GMT+0100) Europe/Budapest'), (b'Europe/Copenhagen', b'(GMT+0100) Europe/Copenhagen'), (b'Europe/Gibraltar', b'(GMT+0100) Europe/Gibraltar'), (b'Europe/Ljubljana', b'(GMT+0100) Europe/Ljubljana'), (b'Europe/Luxembourg', b'(GMT+0100) Europe/Luxembourg'), (b'Europe/Madrid', b'(GMT+0100) Europe/Madrid'), (b'Europe/Malta', b'(GMT+0100) Europe/Malta'), (b'Europe/Monaco', b'(GMT+0100) Europe/Monaco'), (b'Europe/Oslo', b'(GMT+0100) Europe/Oslo'), (b'Europe/Paris', b'(GMT+0100) Europe/Paris'), (b'Europe/Podgorica', b'(GMT+0100) Europe/Podgorica'), (b'Europe/Prague', b'(GMT+0100) Europe/Prague'), (b'Europe/Rome', b'(GMT+0100) Europe/Rome'), (b'Europe/San_Marino', b'(GMT+0100) Europe/San_Marino'), (b'Europe/Sarajevo', b'(GMT+0100) Europe/Sarajevo'), (b'Europe/Skopje', b'(GMT+0100) Europe/Skopje'), (b'Europe/Stockholm', b'(GMT+0100) Europe/Stockholm'), (b'Europe/Tirane', b'(GMT+0100) Europe/Tirane'), (b'Europe/Vaduz', b'(GMT+0100) Europe/Vaduz'), (b'Europe/Vatican', b'(GMT+0100) Europe/Vatican'), (b'Europe/Vienna', b'(GMT+0100) Europe/Vienna'), (b'Europe/Warsaw', b'(GMT+0100) Europe/Warsaw'), (b'Europe/Zagreb', b'(GMT+0100) Europe/Zagreb'), (b'Europe/Zurich', b'(GMT+0100) Europe/Zurich'), (b'Africa/Blantyre', b'(GMT+0200) Africa/Blantyre'), (b'Africa/Bujumbura', b'(GMT+0200) Africa/Bujumbura'), (b'Africa/Cairo', b'(GMT+0200) Africa/Cairo'), (b'Africa/Gaborone', b'(GMT+0200) Africa/Gaborone'), (b'Africa/Harare', b'(GMT+0200) Africa/Harare'), (b'Africa/Johannesburg', b'(GMT+0200) Africa/Johannesburg'), (b'Africa/Kigali', b'(GMT+0200) Africa/Kigali'), (b'Africa/Lubumbashi', b'(GMT+0200) Africa/Lubumbashi'), (b'Africa/Lusaka', b'(GMT+0200) Africa/Lusaka'), (b'Africa/Maputo', b'(GMT+0200) Africa/Maputo'), (b'Africa/Maseru', b'(GMT+0200) Africa/Maseru'), (b'Africa/Mbabane', b'(GMT+0200) Africa/Mbabane'), (b'Africa/Tripoli', b'(GMT+0200) Africa/Tripoli'), (b'Africa/Windhoek', b'(GMT+0200) Africa/Windhoek'), (b'Asia/Amman', b'(GMT+0200) Asia/Amman'), (b'Asia/Beirut', b'(GMT+0200) Asia/Beirut'), (b'Asia/Damascus', b'(GMT+0200) Asia/Damascus'), (b'Asia/Gaza', b'(GMT+0200) Asia/Gaza'), (b'Asia/Hebron', b'(GMT+0200) Asia/Hebron'), (b'Asia/Jerusalem', b'(GMT+0200) Asia/Jerusalem'), (b'Asia/Nicosia', b'(GMT+0200) Asia/Nicosia'), (b'Europe/Athens', b'(GMT+0200) Europe/Athens'), (b'Europe/Bucharest', b'(GMT+0200) Europe/Bucharest'), (b'Europe/Chisinau', b'(GMT+0200) Europe/Chisinau'), (b'Europe/Helsinki', b'(GMT+0200) Europe/Helsinki'), (b'Europe/Istanbul', b'(GMT+0200) Europe/Istanbul'), (b'Europe/Kiev', b'(GMT+0200) Europe/Kiev'), (b'Europe/Mariehamn', b'(GMT+0200) Europe/Mariehamn'), (b'Europe/Riga', b'(GMT+0200) Europe/Riga'), (b'Europe/Sofia', b'(GMT+0200) Europe/Sofia'), (b'Europe/Tallinn', b'(GMT+0200) Europe/Tallinn'), (b'Europe/Uzhgorod', b'(GMT+0200) Europe/Uzhgorod'), (b'Europe/Vilnius', b'(GMT+0200) Europe/Vilnius'), (b'Europe/Zaporozhye', b'(GMT+0200) Europe/Zaporozhye'), (b'Africa/Addis_Ababa', b'(GMT+0300) Africa/Addis_Ababa'), (b'Africa/Asmara', b'(GMT+0300) Africa/Asmara'), (b'Africa/Dar_es_Salaam', b'(GMT+0300) Africa/Dar_es_Salaam'), (b'Africa/Djibouti', b'(GMT+0300) Africa/Djibouti'), (b'Africa/Juba', b'(GMT+0300) Africa/Juba'), (b'Africa/Kampala', b'(GMT+0300) Africa/Kampala'), (b'Africa/Khartoum', b'(GMT+0300) Africa/Khartoum'), (b'Africa/Mogadishu', b'(GMT+0300) Africa/Mogadishu'), (b'Africa/Nairobi', b'(GMT+0300) Africa/Nairobi'), (b'Antarctica/Syowa', b'(GMT+0300) Antarctica/Syowa'), (b'Asia/Aden', b'(GMT+0300) Asia/Aden'), (b'Asia/Baghdad', b'(GMT+0300) Asia/Baghdad'), (b'Asia/Bahrain', b'(GMT+0300) Asia/Bahrain'), (b'Asia/Kuwait', b'(GMT+0300) Asia/Kuwait'), (b'Asia/Qatar', b'(GMT+0300) Asia/Qatar'), (b'Asia/Riyadh', b'(GMT+0300) Asia/Riyadh'), (b'Europe/Kaliningrad', b'(GMT+0300) Europe/Kaliningrad'), (b'Europe/Minsk', b'(GMT+0300) Europe/Minsk'), (b'Indian/Antananarivo', b'(GMT+0300) Indian/Antananarivo'), (b'Indian/Comoro', b'(GMT+0300) Indian/Comoro'), (b'Indian/Mayotte', b'(GMT+0300) Indian/Mayotte'), (b'Asia/Tehran', b'(GMT+0330) Asia/Tehran'), (b'Asia/Baku', b'(GMT+0400) Asia/Baku'), (b'Asia/Dubai', b'(GMT+0400) Asia/Dubai'), (b'Asia/Muscat', b'(GMT+0400) Asia/Muscat'), (b'Asia/Tbilisi', b'(GMT+0400) Asia/Tbilisi'), (b'Asia/Yerevan', b'(GMT+0400) Asia/Yerevan'), (b'Europe/Moscow', b'(GMT+0400) Europe/Moscow'), (b'Europe/Samara', b'(GMT+0400) Europe/Samara'), (b'Europe/Simferopol', b'(GMT+0400) Europe/Simferopol'), (b'Europe/Volgograd', b'(GMT+0400) Europe/Volgograd'), (b'Indian/Mahe', b'(GMT+0400) Indian/Mahe'), (b'Indian/Mauritius', b'(GMT+0400) Indian/Mauritius'), (b'Indian/Reunion', b'(GMT+0400) Indian/Reunion'), (b'Asia/Kabul', b'(GMT+0430) Asia/Kabul'), (b'Antarctica/Mawson', b'(GMT+0500) Antarctica/Mawson'), (b'Asia/Aqtau', b'(GMT+0500) Asia/Aqtau'), (b'Asia/Aqtobe', b'(GMT+0500) Asia/Aqtobe'), (b'Asia/Ashgabat', b'(GMT+0500) Asia/Ashgabat'), (b'Asia/Dushanbe', b'(GMT+0500) Asia/Dushanbe'), (b'Asia/Karachi', b'(GMT+0500) Asia/Karachi'), (b'Asia/Oral', b'(GMT+0500) Asia/Oral'), (b'Asia/Samarkand', b'(GMT+0500) Asia/Samarkand'), (b'Asia/Tashkent', b'(GMT+0500) Asia/Tashkent'), (b'Indian/Kerguelen', b'(GMT+0500) Indian/Kerguelen'), (b'Indian/Maldives', b'(GMT+0500) Indian/Maldives'), (b'Asia/Colombo', b'(GMT+0530) Asia/Colombo'), (b'Asia/Kolkata', b'(GMT+0530) Asia/Kolkata'), (b'Asia/Kathmandu', b'(GMT+0545) Asia/Kathmandu'), (b'Antarctica/Vostok', b'(GMT+0600) Antarctica/Vostok'), (b'Asia/Almaty', b'(GMT+0600) Asia/Almaty'), (b'Asia/Bishkek', b'(GMT+0600) Asia/Bishkek'), (b'Asia/Dhaka', b'(GMT+0600) Asia/Dhaka'), (b'Asia/Qyzylorda', b'(GMT+0600) Asia/Qyzylorda'), (b'Asia/Thimphu', b'(GMT+0600) Asia/Thimphu'), (b'Asia/Yekaterinburg', b'(GMT+0600) Asia/Yekaterinburg'), (b'Indian/Chagos', b'(GMT+0600) Indian/Chagos'), (b'Asia/Rangoon', b'(GMT+0630) Asia/Rangoon'), (b'Indian/Cocos', b'(GMT+0630) Indian/Cocos'), (b'Antarctica/Davis', b'(GMT+0700) Antarctica/Davis'), (b'Asia/Bangkok', b'(GMT+0700) Asia/Bangkok'), (b'Asia/Ho_Chi_Minh', b'(GMT+0700) Asia/Ho_Chi_Minh'), (b'Asia/Hovd', b'(GMT+0700) Asia/Hovd'), (b'Asia/Jakarta', b'(GMT+0700) Asia/Jakarta'), (b'Asia/Novokuznetsk', b'(GMT+0700) Asia/Novokuznetsk'), (b'Asia/Novosibirsk', b'(GMT+0700) Asia/Novosibirsk'), (b'Asia/Omsk', b'(GMT+0700) Asia/Omsk'), (b'Asia/Phnom_Penh', b'(GMT+0700) Asia/Phnom_Penh'), (b'Asia/Pontianak', b'(GMT+0700) Asia/Pontianak'), (b'Asia/Vientiane', b'(GMT+0700) Asia/Vientiane'), (b'Indian/Christmas', b'(GMT+0700) Indian/Christmas'), (b'Antarctica/Casey', b'(GMT+0800) Antarctica/Casey'), (b'Asia/Brunei', b'(GMT+0800) Asia/Brunei'), (b'Asia/Choibalsan', b'(GMT+0800) Asia/Choibalsan'), (b'Asia/Chongqing', b'(GMT+0800) Asia/Chongqing'), (b'Asia/Harbin', b'(GMT+0800) Asia/Harbin'), (b'Asia/Hong_Kong', b'(GMT+0800) Asia/Hong_Kong'), (b'Asia/Kashgar', b'(GMT+0800) Asia/Kashgar'), (b'Asia/Krasnoyarsk', b'(GMT+0800) Asia/Krasnoyarsk'), (b'Asia/Kuala_Lumpur', b'(GMT+0800) Asia/Kuala_Lumpur'), (b'Asia/Kuching', b'(GMT+0800) Asia/Kuching'), (b'Asia/Macau', b'(GMT+0800) Asia/Macau'), (b'Asia/Makassar', b'(GMT+0800) Asia/Makassar'), (b'Asia/Manila', b'(GMT+0800) Asia/Manila'), (b'Asia/Shanghai', b'(GMT+0800) Asia/Shanghai'), (b'Asia/Singapore', b'(GMT+0800) Asia/Singapore'), (b'Asia/Taipei', b'(GMT+0800) Asia/Taipei'), (b'Asia/Ulaanbaatar', b'(GMT+0800) Asia/Ulaanbaatar'), (b'Asia/Urumqi', b'(GMT+0800) Asia/Urumqi'), (b'Australia/Perth', b'(GMT+0800) Australia/Perth'), (b'Australia/Eucla', b'(GMT+0845) Australia/Eucla'), (b'Asia/Dili', b'(GMT+0900) Asia/Dili'), (b'Asia/Irkutsk', b'(GMT+0900) Asia/Irkutsk'), (b'Asia/Jayapura', b'(GMT+0900) Asia/Jayapura'), (b'Asia/Pyongyang', b'(GMT+0900) Asia/Pyongyang'), (b'Asia/Seoul', b'(GMT+0900) Asia/Seoul'), (b'Asia/Tokyo', b'(GMT+0900) Asia/Tokyo'), (b'Pacific/Palau', b'(GMT+0900) Pacific/Palau'), (b'Australia/Darwin', b'(GMT+0930) Australia/Darwin'), (b'Antarctica/DumontDUrville', b'(GMT+1000) Antarctica/DumontDUrville'), (b'Asia/Yakutsk', b'(GMT+1000) Asia/Yakutsk'), (b'Australia/Brisbane', b'(GMT+1000) Australia/Brisbane'), (b'Australia/Lindeman', b'(GMT+1000) Australia/Lindeman'), (b'Pacific/Chuuk', b'(GMT+1000) Pacific/Chuuk'), (b'Pacific/Guam', b'(GMT+1000) Pacific/Guam'), (b'Pacific/Port_Moresby', b'(GMT+1000) Pacific/Port_Moresby'), (b'Pacific/Saipan', b'(GMT+1000) Pacific/Saipan'), (b'Australia/Adelaide', b'(GMT+1030) Australia/Adelaide'), (b'Australia/Broken_Hill', b'(GMT+1030) Australia/Broken_Hill'), (b'Antarctica/Macquarie', b'(GMT+1100) Antarctica/Macquarie'), (b'Asia/Sakhalin', b'(GMT+1100) Asia/Sakhalin'), (b'Asia/Vladivostok', b'(GMT+1100) Asia/Vladivostok'), (b'Australia/Currie', b'(GMT+1100) Australia/Currie'), (b'Australia/Hobart', b'(GMT+1100) Australia/Hobart'), (b'Australia/Lord_Howe', b'(GMT+1100) Australia/Lord_Howe'), (b'Australia/Melbourne', b'(GMT+1100) Australia/Melbourne'), (b'Australia/Sydney', b'(GMT+1100) Australia/Sydney'), (b'Pacific/Efate', b'(GMT+1100) Pacific/Efate'), (b'Pacific/Guadalcanal', b'(GMT+1100) Pacific/Guadalcanal'), (b'Pacific/Kosrae', b'(GMT+1100) Pacific/Kosrae'), (b'Pacific/Noumea', b'(GMT+1100) Pacific/Noumea'), (b'Pacific/Pohnpei', b'(GMT+1100) Pacific/Pohnpei'), (b'Pacific/Norfolk', b'(GMT+1130) Pacific/Norfolk'), (b'Asia/Anadyr', b'(GMT+1200) Asia/Anadyr'), (b'Asia/Kamchatka', b'(GMT+1200) Asia/Kamchatka'), (b'Asia/Magadan', b'(GMT+1200) Asia/Magadan'), (b'Pacific/Fiji', b'(GMT+1200) Pacific/Fiji'), (b'Pacific/Funafuti', b'(GMT+1200) Pacific/Funafuti'), (b'Pacific/Kwajalein', b'(GMT+1200) Pacific/Kwajalein'), (b'Pacific/Majuro', b'(GMT+1200) Pacific/Majuro'), (b'Pacific/Nauru', b'(GMT+1200) Pacific/Nauru'), (b'Pacific/Tarawa', b'(GMT+1200) Pacific/Tarawa'), (b'Pacific/Wake', b'(GMT+1200) Pacific/Wake'), (b'Pacific/Wallis', b'(GMT+1200) Pacific/Wallis'), (b'Antarctica/McMurdo', b'(GMT+1300) Antarctica/McMurdo'), (b'Antarctica/South_Pole', b'(GMT+1300) Antarctica/South_Pole'), (b'Pacific/Auckland', b'(GMT+1300) Pacific/Auckland'), (b'Pacific/Enderbury', b'(GMT+1300) Pacific/Enderbury'), (b'Pacific/Fakaofo', b'(GMT+1300) Pacific/Fakaofo'), (b'Pacific/Tongatapu', b'(GMT+1300) Pacific/Tongatapu'), (b'Pacific/Chatham', b'(GMT+1345) Pacific/Chatham'), (b'Pacific/Apia', b'(GMT+1400) Pacific/Apia'), (b'Pacific/Kiritimati', b'(GMT+1400) Pacific/Kiritimati')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('kind', models.CharField(default=b'besteffort', max_length=30, choices=[
                 (b'besteffort', b'besteffort'), (b'reservation', b'reservation'), (b'monthlyfee', b'monthlyfee')])),
                ('state', models.CharField(default=b'pending', max_length=30, choices=[
                 (b'pending', b'pending'), (b'invoiced', b'invoiced')])),
                ('date', models.DateTimeField()),
                ('amount', models.FloatField(default=0.0)),
                ('coreHours', models.FloatField(default=0.0)),
                ('account', models.ForeignKey(
                    related_name=b'charges', to='core.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(
                    help_text=b'Name of the Controller', unique=True, max_length=200)),
                ('backend_type', models.CharField(
                    help_text=b'Type of compute controller, e.g. EC2, OpenStack, or OpenStack version', max_length=200)),
                ('version', models.CharField(
                    help_text=b'Controller version', max_length=200)),
                ('auth_url', models.CharField(
                    help_text=b'Auth url for the compute controller', max_length=200, null=True, blank=True)),
                ('admin_user', models.CharField(
                    help_text=b'Username of an admin user at this controller', max_length=200, null=True, blank=True)),
                ('admin_password', models.CharField(
                    help_text=b'Password of theadmin user at this controller', max_length=200, null=True, blank=True)),
                ('admin_tenant', models.CharField(
                    help_text=b'Name of the tenant the admin user belongs to', max_length=200, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerCredential',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.SlugField(
                    help_text=b'The credential type, e.g. ec2', max_length=128)),
                ('key_id', models.CharField(
                    help_text=b'The backend id of this credential', max_length=1024)),
                ('enc_value', encrypted_fields.fields.EncryptedCharField(
                    help_text=b'The key value of this credential', max_length=1024)),
                ('controller', models.ForeignKey(related_name=b'controllercredentials',
                                                 to='core.Controller', help_text=b'The User this credential is associated with')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerDashboardView',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('enabled', models.BooleanField(default=True)),
                ('url', models.CharField(help_text=b'URL of Dashboard', max_length=1024)),
                ('controller', models.ForeignKey(
                    related_name=b'controllerdashboardviews', to='core.Controller')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('glance_image_id', models.CharField(
                    help_text=b'Glance image id', max_length=200, null=True, blank=True)),
                ('controller', models.ForeignKey(
                    related_name=b'controllerimages', to='core.Controller')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerNetwork',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('net_id', models.CharField(help_text=b'Quantum network',
                                            max_length=256, null=True, blank=True)),
                ('router_id', models.CharField(help_text=b'Quantum router id',
                                               max_length=256, null=True, blank=True)),
                ('subnet_id', models.CharField(help_text=b'Quantum subnet id',
                                               max_length=256, null=True, blank=True)),
                ('subnet', models.CharField(max_length=32, blank=True)),
                ('controller', models.ForeignKey(
                    related_name=b'controllernetworks', to='core.Controller')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('role', models.CharField(unique=True,
                                          max_length=30, choices=[(b'admin', b'Admin')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('tenant_id', models.CharField(help_text=b'Keystone tenant id',
                                               max_length=200, null=True, db_index=True, blank=True)),
                ('controller', models.ForeignKey(related_name=b'controllersite',
                                                 blank=True, to='core.Controller', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerSitePrivilege',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('role_id', models.CharField(help_text=b'Keystone id',
                                             max_length=200, null=True, db_index=True, blank=True)),
                ('controller', models.ForeignKey(
                    related_name=b'controllersiteprivileges', to='core.Controller')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerSlice',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('tenant_id', models.CharField(
                    help_text=b'Keystone tenant id', max_length=200, null=True, blank=True)),
                ('controller', models.ForeignKey(
                    related_name=b'controllerslices', to='core.Controller')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerSlicePrivilege',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('role_id', models.CharField(help_text=b'Keystone id',
                                             max_length=200, null=True, db_index=True, blank=True)),
                ('controller', models.ForeignKey(
                    related_name=b'controllersliceprivileges', to='core.Controller')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ControllerUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('kuser_id', models.CharField(help_text=b'Keystone user id',
                                              max_length=200, null=True, blank=True)),
                ('controller', models.ForeignKey(
                    related_name=b'controllersusers', to='core.Controller')),
                ('user', models.ForeignKey(
                    related_name=b'controllerusers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DashboardView',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(
                    help_text=b'Name of the View', unique=True, max_length=200)),
                ('url', models.CharField(help_text=b'URL of Dashboard', max_length=1024)),
                ('enabled', models.BooleanField(default=True)),
                ('controllers', models.ManyToManyField(related_name=b'dashboardviews',
                                                       through='core.ControllerDashboardView', to='core.Controller', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(
                    help_text=b'Name of the Deployment', unique=True, max_length=200)),
                ('accessControl', models.TextField(default=b'allow all',
                                                   help_text=b'Access control list that specifies which sites/users may use nodes in this deployment', max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeploymentPrivilege',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('deployment', models.ForeignKey(
                    related_name=b'deploymentprivileges', to='core.Deployment')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeploymentRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('role', models.CharField(unique=True,
                                          max_length=30, choices=[(b'admin', b'Admin')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(
                    help_text=b'name of this flavor, as displayed to users', max_length=32)),
                ('description', models.CharField(
                    max_length=1024, null=True, blank=True)),
                ('flavor', models.CharField(
                    help_text=b'flavor string used to configure deployments', max_length=32)),
                ('order', models.IntegerField(default=0,
                                              help_text=b'used to order flavors when displayed in a list')),
                ('default', models.BooleanField(default=False,
                                                help_text=b'make this a default flavor to use when creating new instances')),
                ('deployments', models.ManyToManyField(
                    related_name=b'flavors', to='core.Deployment', blank=True)),
            ],
            options={
                'ordering': ('order', 'name'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(unique=True, max_length=256)),
                ('disk_format', models.CharField(max_length=256)),
                ('container_format', models.CharField(max_length=256)),
                ('path', models.CharField(help_text=b'Path to image on local disk',
                                          max_length=256, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageDeployments',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('deployment', models.ForeignKey(
                    related_name=b'imagedeployments', to='core.Deployment')),
                ('image', models.ForeignKey(
                    related_name=b'imagedeployments', to='core.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('date', models.DateTimeField()),
                ('account', models.ForeignKey(
                    related_name=b'invoices', to='core.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('subnet', models.CharField(max_length=32, blank=True)),
                ('ports', models.CharField(blank=True, max_length=1024,
                                           null=True, validators=[core.models.network.ValidateNatList])),
                ('labels', models.CharField(max_length=1024, null=True, blank=True)),
                ('guaranteed_bandwidth', models.IntegerField(default=0)),
                ('permit_all_slices', models.BooleanField(default=False)),
                ('topology_parameters', models.TextField(null=True, blank=True)),
                ('controller_url', models.CharField(
                    max_length=1024, null=True, blank=True)),
                ('controller_parameters', models.TextField(null=True, blank=True)),
                ('network_id', models.CharField(help_text=b'Quantum network',
                                                max_length=256, null=True, blank=True)),
                ('router_id', models.CharField(help_text=b'Quantum router id',
                                               max_length=256, null=True, blank=True)),
                ('subnet_id', models.CharField(help_text=b'Quantum subnet id',
                                               max_length=256, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NetworkParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('value', models.CharField(
                    help_text=b'The value of this parameter', max_length=1024)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NetworkParameterType',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.SlugField(
                    help_text=b'The name of this parameter', max_length=128)),
                ('description', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NetworkSlice',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('network', models.ForeignKey(
                    related_name=b'networkslices', to='core.Network')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NetworkInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('ip', models.GenericIPAddressField(
                    help_text=b'Instance ip address', null=True, blank=True)),
                ('port_id', models.CharField(help_text=b'Quantum port id',
                                             max_length=256, null=True, blank=True)),
                ('network', models.ForeignKey(
                    related_name=b'networkinstances', to='core.Network')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NetworkTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(
                    max_length=1024, null=True, blank=True)),
                ('guaranteed_bandwidth', models.IntegerField(default=0)),
                ('visibility', models.CharField(default=b'private', max_length=30,
                                                choices=[(b'public', b'public'), (b'private', b'private')])),
                ('translation', models.CharField(default=b'none', max_length=30,
                                                 choices=[(b'none', b'none'), (b'NAT', b'NAT')])),
                ('shared_network_name', models.CharField(
                    max_length=30, null=True, blank=True)),
                ('shared_network_id', models.CharField(
                    help_text=b'Quantum network', max_length=256, null=True, blank=True)),
                ('topology_kind', models.CharField(default=b'BigSwitch', max_length=30, choices=[
                 (b'bigswitch', b'BigSwitch'), (b'physical', b'Physical'), (b'custom', b'Custom')])),
                ('controller_kind', models.CharField(default=None, max_length=30, null=True,
                                                     blank=True, choices=[(None, b'None'), (b'onos', b'ONOS'), (b'custom', b'Custom')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(
                    help_text=b'Name of the Node', unique=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0.0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(
                    related_name=b'payments', to='core.Account')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanetStack',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('description', models.CharField(default=b'PlanetStack',
                                                 help_text=b'Used for scoping of roles at the PlanetStack Application level', unique=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'PlanetStack',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanetStackPrivilege',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('planetstack', models.ForeignKey(
                    related_name=b'planetstackprivileges', default=1, to='core.PlanetStack')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanetStackRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('role', models.CharField(unique=True,
                                          max_length=30, choices=[(b'admin', b'Admin')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(
                    help_text=b'Name of Project', unique=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('startTime', models.DateTimeField()),
                ('duration', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReservedResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('reservationSet', models.ForeignKey(
                    related_name=b'reservedresources', to='core.Reservation')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Reserved Resources',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('role_type', models.CharField(max_length=80, verbose_name=b'Name')),
                ('role', models.CharField(max_length=80, null=True,
                                          verbose_name=b'Keystone role id', blank=True)),
                ('description', models.CharField(
                    max_length=120, verbose_name=b'Description')),
                ('content_type', models.ForeignKey(
                    verbose_name=b'Role Scope', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('networks', models.ManyToManyField(
                    related_name=b'routers', to='core.Network', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('description', models.TextField(
                    help_text=b'Description of Service', max_length=254, null=True, blank=True)),
                ('enabled', models.BooleanField(default=True)),
                ('name', models.CharField(help_text=b'Service Name', max_length=30)),
                ('versionNumber', models.CharField(
                    help_text=b'Version of Service Definition', max_length=30)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.SlugField(help_text=b'Attribute Name', max_length=128)),
                ('value', models.CharField(
                    help_text=b'Attribute Value', max_length=1024)),
                ('service', models.ForeignKey(related_name=b'serviceattributes',
                                              to='core.Service', help_text=b'The Service this attribute is associated with')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=255)),
                ('commitment', models.IntegerField(default=365)),
                ('membershipFee', models.IntegerField(default=0)),
                ('membershipFeeMonths', models.IntegerField(default=12)),
                ('upgradeRequiresApproval', models.BooleanField(default=False)),
                ('upgradeFrom', models.ManyToManyField(
                    related_name='upgradeFrom_rel_+', null=True, to='core.ServiceClass', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Service classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32)),
                ('maxUnitsDeployment', models.IntegerField(default=1)),
                ('maxUnitsNode', models.IntegerField(default=1)),
                ('maxDuration', models.IntegerField(default=1)),
                ('bucketInRate', models.IntegerField(default=0)),
                ('bucketMaxSize', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('calendarReservable', models.BooleanField(default=True)),
                ('serviceClass', models.ForeignKey(
                    related_name=b'serviceresources', to='core.ServiceClass')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(
                    help_text=b'Name for this Site', max_length=200)),
                ('site_url', models.URLField(help_text=b"Site's Home URL Page",
                                             max_length=512, null=True, blank=True)),
                ('enabled', models.BooleanField(
                    default=True, help_text=b'Status for this Site')),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('login_base', models.CharField(
                    help_text=b'Prefix for Slices associated with this Site', unique=True, max_length=50)),
                ('is_public', models.BooleanField(
                    default=True, help_text=b'Indicates the visibility of this site to other members')),
                ('abbreviated_name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteCredential',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.SlugField(
                    help_text=b'The credential type, e.g. ec2', max_length=128)),
                ('key_id', models.CharField(
                    help_text=b'The backend id of this credential', max_length=1024)),
                ('enc_value', encrypted_fields.fields.EncryptedCharField(
                    help_text=b'The key value of this credential', max_length=1024)),
                ('site', models.ForeignKey(related_name=b'sitecredentials', to='core.Site',
                                           help_text=b'The User this credential is associated with')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteDeployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('availability_zone', models.CharField(
                    help_text=b'OpenStack availability zone', max_length=200, null=True, blank=True)),
                ('controller', models.ForeignKey(
                    related_name=b'sitedeployments', blank=True, to='core.Controller', null=True)),
                ('deployment', models.ForeignKey(
                    related_name=b'sitedeployments', to='core.Deployment')),
                ('site', models.ForeignKey(
                    related_name=b'sitedeployments', to='core.Site')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SitePrivilege',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('role', models.CharField(unique=True, max_length=30, choices=[
                 (b'admin', b'Admin'), (b'pi', b'PI'), (b'tech', b'Tech'), (b'billing', b'Billing')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slice',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(
                    help_text=b'The Name of the Slice', unique=True, max_length=80)),
                ('enabled', models.BooleanField(
                    default=True, help_text=b'Status for this Slice')),
                ('omf_friendly', models.BooleanField(default=False)),
                ('description', models.TextField(
                    help_text=b'High level description of the slice and expected activities', max_length=1024, blank=True)),
                ('slice_url', models.URLField(max_length=512, blank=True)),
                ('max_instances', models.IntegerField(default=10)),
                ('network', models.CharField(default=b'Private Only',
                                             max_length=256, null=True, blank=True)),
                ('mount_data_sets', models.CharField(
                    default=b'GenBank', max_length=256, null=True, blank=True)),
                ('creator', models.ForeignKey(related_name=b'slices',
                                              blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('default_flavor', models.ForeignKey(
                    related_name=b'slices', blank=True, to='core.Flavor', null=True)),
                ('default_image', models.ForeignKey(
                    related_name=b'slices', blank=True, to='core.Image', null=True)),
                ('service', models.ForeignKey(related_name=b'service',
                                              blank=True, to='core.Service', null=True)),
                ('serviceClass', models.ForeignKey(related_name=b'slices',
                                                   default=core.models.serviceclass.get_default_serviceclass, to='core.ServiceClass', null=True)),
                ('site', models.ForeignKey(related_name=b'slices',
                                           to='core.Site', help_text=b'The Site this Slice belongs to')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SliceCredential',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.SlugField(
                    help_text=b'The credential type, e.g. ec2', max_length=128)),
                ('key_id', models.CharField(
                    help_text=b'The backend id of this credential', max_length=1024)),
                ('enc_value', encrypted_fields.fields.EncryptedCharField(
                    help_text=b'The key value of this credential', max_length=1024)),
                ('slice', models.ForeignKey(related_name=b'slicecredentials',
                                            to='core.Slice', help_text=b'The User this credential is associated with')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SlicePrivilege',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SliceRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('role', models.CharField(unique=True, max_length=30,
                                          choices=[(b'admin', b'Admin'), (b'default', b'Default')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SliceTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(help_text=b'The name of this tag', max_length=30, choices=[
                 (b'privatekey', b'Private Key'), (b'publickey', b'Public Key')])),
                ('value', models.CharField(
                    help_text=b'The value of this tag', max_length=1024)),
                ('slice', models.ForeignKey(
                    related_name=b'slicetags', to='core.Slice')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('instance_id', models.CharField(
                    help_text=b'Nova instance id', max_length=200, null=True, blank=True)),
                ('instance_uuid', models.CharField(
                    help_text=b'Nova instance uuid', max_length=200, null=True, blank=True)),
                ('name', models.CharField(help_text=b'Instance name', max_length=200)),
                ('instance_name', models.CharField(
                    help_text=b'OpenStack generated name', max_length=200, null=True, blank=True)),
                ('ip', models.GenericIPAddressField(
                    help_text=b'Instance ip address', null=True, blank=True)),
                ('numberCores', models.IntegerField(
                    default=0, help_text=b'Number of cores for instance', verbose_name=b'Number of Cores')),
                ('userData', models.TextField(
                    help_text=b'user_data passed to instance during creation', null=True, blank=True)),
                ('creator', models.ForeignKey(related_name=b'instances',
                                              blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('deployment', models.ForeignKey(related_name=b'instance_deployment',
                                                 verbose_name=b'deployment', to='core.Deployment')),
                ('flavor', models.ForeignKey(default=core.models.instance.get_default_flavor,
                                             to='core.Flavor', help_text=b'Flavor of this instance')),
                ('image', models.ForeignKey(
                    related_name=b'instances', to='core.Image')),
                ('node', models.ForeignKey(related_name=b'instances', to='core.Node')),
                ('slice', models.ForeignKey(
                    related_name=b'instances', to='core.Slice')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.SlugField(
                    help_text=b'The name of this tag', max_length=128)),
                ('value', models.CharField(
                    help_text=b'The value of this tag', max_length=1024)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('service', models.ForeignKey(related_name=b'tags', to='core.Service',
                                              help_text=b'The Service this Tag is associated with')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UsableObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCredential',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.SlugField(
                    help_text=b'The credential type, e.g. ec2', max_length=128)),
                ('key_id', models.CharField(
                    help_text=b'The backend id of this credential', max_length=1024)),
                ('enc_value', encrypted_fields.fields.EncryptedCharField(
                    help_text=b'The key value of this credential', max_length=1024)),
                ('user', models.ForeignKey(related_name=b'usercredentials', to=settings.AUTH_USER_MODEL,
                                           help_text=b'The User this credential is associated with')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDashboardView',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('dashboardView', models.ForeignKey(
                    related_name=b'userdashboardviews', to='core.DashboardView')),
                ('user', models.ForeignKey(
                    related_name=b'userdashboardviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TenantPrivilege',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TenantRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now_add=True)),
                ('updated', models.DateTimeField(
                    default=django.utils.timezone.now, auto_now=True)),
                ('enacted', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('policed', models.DateTimeField(
                    default=None, null=True, blank=True)),
                ('backend_status', models.CharField(
                    default=b'Provisioning in progress', max_length=140)),
                ('deleted', models.BooleanField(default=False)),
                ('role', models.CharField(unique=True, max_length=30,
                                          choices=[(b'admin', b'Admin'), (b'access', b'Access')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sliceprivilege',
            name='role',
            field=models.ForeignKey(
                related_name=b'sliceprivileges', to='core.SliceRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sliceprivilege',
            name='slice',
            field=models.ForeignKey(
                related_name=b'sliceprivileges', to='core.Slice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sliceprivilege',
            name='user',
            field=models.ForeignKey(
                related_name=b'sliceprivileges', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='siteprivilege',
            name='role',
            field=models.ForeignKey(
                related_name=b'siteprivileges', to='core.SiteRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='siteprivilege',
            name='site',
            field=models.ForeignKey(
                related_name=b'siteprivileges', to='core.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='siteprivilege',
            name='user',
            field=models.ForeignKey(
                related_name=b'siteprivileges', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='deployments',
            field=models.ManyToManyField(help_text=b'Select which sites are allowed to host nodes in this deployment',
                                         related_name=b'sites', through='core.SiteDeployment', to='core.Deployment', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='router',
            name='owner',
            field=models.ForeignKey(related_name=b'routers', to='core.Slice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='router',
            name='permittedNetworks',
            field=models.ManyToManyField(
                related_name=b'availableRouters', to='core.Network', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reservedresource',
            name='resource',
            field=models.ForeignKey(
                related_name=b'reservedresources', to='core.ServiceResource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reservedresource',
            name='instance',
            field=models.ForeignKey(
                related_name=b'reservedresources', to='core.Instance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reservation',
            name='slice',
            field=models.ForeignKey(
                related_name=b'reservations', to='core.Slice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planetstackprivilege',
            name='role',
            field=models.ForeignKey(to='core.PlanetStackRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='planetstackprivilege',
            name='user',
            field=models.ForeignKey(
                related_name=b'planetstackprivileges', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='node',
            name='site',
            field=models.ForeignKey(
                related_name=b'nodes', blank=True, to='core.Site', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='node',
            name='site_deployment',
            field=models.ForeignKey(
                related_name=b'nodes', to='core.SiteDeployment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='networkinstance',
            name='instance',
            field=models.ForeignKey(
                related_name=b'networkinstances', to='core.Instance'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='networkslice',
            name='slice',
            field=models.ForeignKey(
                related_name=b'networkslices', to='core.Slice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='networkparameter',
            name='parameter',
            field=models.ForeignKey(related_name=b'networkparameters',
                                    to='core.NetworkParameterType', help_text=b'The type of the parameter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='network',
            name='owner',
            field=models.ForeignKey(related_name=b'ownedNetworks', to='core.Slice',
                                    help_text=b'Slice that owns control of this Network'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='network',
            name='permitted_slices',
            field=models.ManyToManyField(
                related_name=b'availableNetworks', to='core.Slice', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='network',
            name='slices',
            field=models.ManyToManyField(
                related_name=b'networks', through='core.NetworkSlice', to='core.Slice', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='network',
            name='instances',
            field=models.ManyToManyField(
                related_name=b'networks', through='core.NetworkInstance', to='core.Instance', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='network',
            name='template',
            field=models.ForeignKey(to='core.NetworkTemplate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='deployments',
            field=models.ManyToManyField(help_text=b'Select which images should be instantiated on this deployment',
                                         related_name=b'images', through='core.ImageDeployments', to='core.Deployment', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deploymentprivilege',
            name='role',
            field=models.ForeignKey(
                related_name=b'deploymentprivileges', to='core.DeploymentRole'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deploymentprivilege',
            name='user',
            field=models.ForeignKey(
                related_name=b'deploymentprivileges', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='controllersliceprivilege',
            name='slice_privilege',
            field=models.ForeignKey(
                related_name=b'controllersliceprivileges', to='core.SlicePrivilege'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='controllerslice',
            name='slice',
            field=models.ForeignKey(
                related_name=b'controllerslices', to='core.Slice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='controllersiteprivilege',
            name='site_privilege',
            field=models.ForeignKey(
                related_name=b'controllersiteprivileges', to='core.SitePrivilege'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='controllersite',
            name='site',
            field=models.ForeignKey(
                related_name=b'controllersite', to='core.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='controllernetwork',
            name='network',
            field=models.ForeignKey(
                related_name=b'controllernetworks', to='core.Network'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='controllerimages',
            name='image',
            field=models.ForeignKey(
                related_name=b'controllerimages', to='core.Image'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='controllerdashboardview',
            name='dashboardView',
            field=models.ForeignKey(
                related_name=b'controllerdashboardviews', to='core.DashboardView'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='charge',
            name='invoice',
            field=models.ForeignKey(
                related_name=b'charges', blank=True, to='core.Invoice', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='charge',
            name='object',
            field=models.ForeignKey(to='core.UsableObject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='charge',
            name='slice',
            field=models.ForeignKey(
                related_name=b'charges', blank=True, to='core.Slice', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='site',
            field=models.ForeignKey(
                related_name=b'accounts', to='core.Site', help_text=b'Site for this account'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='dashboards',
            field=models.ManyToManyField(
                to='core.DashboardView', through='core.UserDashboardView', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='site',
            field=models.ForeignKey(related_name=b'users', to='core.Site',
                                    help_text=b'Site this user will be homed too', null=True),
            preserve_default=True,
        ),
    ]
