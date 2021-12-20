
# installer for the vds-local extension

from setup import ExtensionInstaller

def loader():
    return MySkinInstaller()

class MySkinInstaller(ExtensionInstaller):
    def __init__(self):
        super(MySkinInstaller, self).__init__(
            version="2.0",
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

                 ('bin/user/vds-local-skin/docs',
                    [
                        'bin/user/vds-local-skin/docs/README.txt',
                        'bin/user/vds-local-skin/docs/convert-json-to-sqlite3.py'
                    ]
                 ),

                 ('bin/user/vds-local-skin/pi',
                    [
                        'bin/user/vds-local-skin/pi/README.txt',
                        'bin/user/vds-local-skin/pi/get-pi-temps.py'
                    ]
                 ),

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
                        'skins/vds-local/gauge.js',
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

                 ( 'skins/vds-local/RGraph/libraries',
                    [
                       'skins/vds-local/RGraph/libraries/RGraph.rscatter.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.annotate.js',
                       'skins/vds-local/RGraph/libraries/RGraph.cornergauge.js',
                       'skins/vds-local/RGraph/libraries/RGraph.hprogress.js',
                       'skins/vds-local/RGraph/libraries/RGraph.drawing.marker1.js',
                       'skins/vds-local/RGraph/libraries/RGraph.funnel.js',
                       'skins/vds-local/RGraph/libraries/jquery.min.js',
                       'skins/vds-local/RGraph/libraries/RGraph.radar.js',
                       'skins/vds-local/RGraph/libraries/RGraph.vprogress.js',
                       'skins/vds-local/RGraph/libraries/RGraph.drawing.xaxis.js',
                       'skins/vds-local/RGraph/libraries/RGraph.led.js',
                       'skins/vds-local/RGraph/libraries/RGraph.drawing.image.js',
                       'skins/vds-local/RGraph/libraries/RGraph.modaldialog.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.effects.js',
                       'skins/vds-local/RGraph/libraries/financial-data.js',
                       'skins/vds-local/RGraph/libraries/RGraph.pie.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.csv.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.tooltips.js',
                       'skins/vds-local/RGraph/libraries/RGraph.fuel.js',
                       'skins/vds-local/RGraph/libraries/RGraph.thermometer.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.zoom.js',
                       'skins/vds-local/RGraph/libraries/RGraph.waterfall.js',
                       'skins/vds-local/RGraph/libraries/RGraph.bar.js',
                       'skins/vds-local/RGraph/libraries/RGraph.hbar.js',
                       'skins/vds-local/RGraph/libraries/RGraph.odo.js',
                       'skins/vds-local/RGraph/libraries/RGraph.drawing.yaxis.js',
                       'skins/vds-local/RGraph/libraries/RGraph.meter.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.resizing.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.key.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.context.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.core.js',
                       'skins/vds-local/RGraph/libraries/RGraph.gantt.js',
                       'skins/vds-local/RGraph/libraries/RGraph.drawing.circle.js',
                       'skins/vds-local/RGraph/libraries/RGraph.drawing.text.js',
                       'skins/vds-local/RGraph/libraries/RGraph.drawing.marker2.js',
                       'skins/vds-local/RGraph/libraries/RGraph.drawing.rect.js',
                       'skins/vds-local/RGraph/libraries/RGraph.bipolar.js',
                       'skins/vds-local/RGraph/libraries/RGraph.drawing.poly.js',
                       'skins/vds-local/RGraph/libraries/RGraph.scatter.js',
                       'skins/vds-local/RGraph/libraries/RGraph.common.dynamic.js',
                       'skins/vds-local/RGraph/libraries/RGraph.line.js',
                       'skins/vds-local/RGraph/libraries/RGraph.rose.js',
                       'skins/vds-local/RGraph/libraries/RGraph.gauge.js',
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
