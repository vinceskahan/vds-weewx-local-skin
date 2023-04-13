## celestial module for weewx skins
## Copyright Tom Keffer, Matthew Wall
## See LICENSE.txt for your rights
#errorCatcher Echo
#encoding UTF-8

## If extended almanac information is available, do extra calculations.
#if $almanac.hasExtras
  ## Pick a "None string" on the basis of whether the sun is above or below the horizon
  #set $sun_altitude = $almanac.sun.alt
  #if $sun_altitude < 0
    #set $sun_None='<i>%s</i>' % $gettext("Always down")
  #else
    #set $sun_None='<i>%s</i>' % $gettext("Always up")
  #end if

  ## For the change in daylight, pick a string to indicate whether it is more or
  ## less than yesterday:
  #set $sun_visible_change = $almanac.sun.visible_change
  #if $sun_visible_change.raw < 0
    #set $change_str = $gettext("less than yesterday")
  #else
    #set $change_str = $gettext("more than yesterday")
  #end if
#end if

<div id="celestial_widget" class="widget">
  </div>
  <div class="widget_contents">
  #if $almanac.hasExtras
	  ##
	  ## note this .inc file just inserts the table row because index.html.tmpl
	  ## includes this file at the end of the current conditions table
	  ##
	  ## see the Seasons skin celestial.inc file for more rows that could be added...
	  ##
          <tr>
            <td class="stats_label">$gettext("Total daylight")</td>
            <td class="stats_data">$almanac.sun.visible<br/>$sun_visible_change $change_str</td>
          </tr>
  #else
            <td class="stats_label">$gettext("Total daylight")</td>
            <td class="stats_data">Install <em>pyephem</em> for detailed celestial timings.</td>
  #end if
  </div>
</div>
