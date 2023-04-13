
# installer for the vds-local extension
#
# note - the 'docs' tree in the sources contains info
#        for how to get the external pi ds18b20 sensors
#        to publish to MQTT.  This tree is not installed
#        onto the runtime weewx system via this installer.
#
#        The bin/user/pi.py extension 'is' no longer installed
#        since we now use MQTTsubscribe to feed the extra
#        sensor readings into weewx.
#

from setup import ExtensionInstaller

def loader():
    return MySkinInstaller()

class MySkinInstaller(ExtensionInstaller):
    def __init__(self):
        super(MySkinInstaller, self).__init__(
            version="2.5",
            name='vds-local',
            description='vds local skin',
            author="Vince Skahan",
            author_email="vinceskahan@gmail.com",
            config={
                'StdReport': {
                    'vds-local': {
                        'skin': 'vds-local',
                        }
                }
            },
            files=[

                 ('skins/vds-local',
                    [
                        'skins/vds-local/000-README.txt',
                        'skins/vds-local/favicon.ico',
                        'skins/vds-local/10year.html.tmpl',
                        'skins/vds-local/10year.css',
                        'skins/vds-local/index.html.tmpl',
                        'skins/vds-local/iphone-pauland.css',
                        'skins/vds-local/month.html.tmpl',
                        'skins/vds-local/phone.html.tmpl',
                        'skins/vds-local/skin.conf',
                        'skins/vds-local/week.html.tmpl',
                        'skins/vds-local/weewx.css',
                        'skins/vds-local/year.html.tmpl',
                        'skins/vds-local/gauge.min.js',
                        'skins/vds-local/alltime.html.tmpl',
                        'skins/vds-local/alltime.css',
                        'skins/vds-local/current.html.tmpl',
                        'skins/vds-local/about.html.tmpl',
                        'skins/vds-local/purpleair.html.tmpl',
                    ],
                 ),

                 ('skins/vds-local/backgrounds',
                    [
                        'skins/vds-local/backgrounds/band.gif',
                    ]
                 ),

                 ( 'skins/vds-local/NOAA',
                    [
                        'skins/vds-local/NOAA/NOAA-YYYY-MM.txt.tmpl',
                        'skins/vds-local/NOAA/NOAA-YYYY.txt.tmpl',
                    ],
                 ),

                 ( 'skins/vds-local/icons',
                    [
                        'skins/vds-local/icons/AF.png',
                        'skins/vds-local/icons/B1n.png',
                        'skins/vds-local/icons/B1.png',
                        'skins/vds-local/icons/B2n.png',
                        'skins/vds-local/icons/B2.png',
                        'skins/vds-local/icons/BD.png',
                        'skins/vds-local/icons/BKn.png',
                        'skins/vds-local/icons/BK.png',
                        'skins/vds-local/icons/blizzard.png',
                        'skins/vds-local/icons/BS.png',
                        'skins/vds-local/icons/CLn.png',
                        'skins/vds-local/icons/CL.png',
                        'skins/vds-local/icons/drizzle.png',
                        'skins/vds-local/icons/E.png',
                        'skins/vds-local/icons/flag.png',
                        'skins/vds-local/icons/flag-yellow.png',
                        'skins/vds-local/icons/flurries.png',
                        'skins/vds-local/icons/F.png',
                        'skins/vds-local/icons/F+.png',
                        'skins/vds-local/icons/frzngdrzl.png',
                        'skins/vds-local/icons/frzngrain.png',
                        'skins/vds-local/icons/FWn.png',
                        'skins/vds-local/icons/FW.png',
                        'skins/vds-local/icons/H.png',
                        'skins/vds-local/icons/K.png',
                        'skins/vds-local/icons/moonphase.png',
                        'skins/vds-local/icons/moon.png',
                        'skins/vds-local/icons/moonriseset.png',
                        'skins/vds-local/icons/NE.png',
                        'skins/vds-local/icons/N.png',
                        'skins/vds-local/icons/NW.png',
                        'skins/vds-local/icons/OVn.png',
                        'skins/vds-local/icons/OV.png',
                        'skins/vds-local/icons/PF.png',
                        'skins/vds-local/icons/PF+.png',
                        'skins/vds-local/icons/pop.png',
                        'skins/vds-local/icons/raindrop.png',
                        'skins/vds-local/icons/rain.png',
                        'skins/vds-local/icons/rainshwrs.png',
                        'skins/vds-local/icons/raintorrent.png',
                        'skins/vds-local/icons/SCn.png',
                        'skins/vds-local/icons/SC.png',
                        'skins/vds-local/icons/SE.png',
                        'skins/vds-local/icons/sleet.png',
                        'skins/vds-local/icons/snowflake.png',
                        'skins/vds-local/icons/snow.png',
                        'skins/vds-local/icons/snowshwrs.png',
                        'skins/vds-local/icons/S.png',
                        'skins/vds-local/icons/sprinkles.png',
                        'skins/vds-local/icons/sunmoon.png',
                        'skins/vds-local/icons/sun.png',
                        'skins/vds-local/icons/sunriseset.png',
                        'skins/vds-local/icons/SW.png',
                        'skins/vds-local/icons/thermometer-blue.png',
                        'skins/vds-local/icons/thermometer-dewpoint.png',
                        'skins/vds-local/icons/thermometer.png',
                        'skins/vds-local/icons/thermometer-red.png',
                        'skins/vds-local/icons/triangle-down.png',
                        'skins/vds-local/icons/triangle-right.png',
                        'skins/vds-local/icons/tstms.png',
                        'skins/vds-local/icons/water.png',
                        'skins/vds-local/icons/W.png',
                    ]
                 )

            ]
         )
