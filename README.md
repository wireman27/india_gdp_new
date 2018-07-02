# Datasets

## Nightlight Imagery

Visible Infrared Imaging Radiometer Suite (VIIRS) Day/Night Band (DNB) Annual Composite for 2015 that removes outliers occurring due to fires and other ephemeral lights, and zeroes out background (non-light) pixels. Each pixel expressed as nanoWatts/cm2/steradian

**Source:** _SVDNB\_npp\_20150101-20151231\_00N060E\_vcm-orm-ntl\_v10\_c201701311200.avg\_rade9.tif_ from [https://bit.ly/2tG5vtg](https://bit.ly/2tG5vtg)

## Population

Global Human Settlement Population Grid for 2015. Each pixel expressed as absolute number of people

**Source:** _GHS\_POP\_GPW42015\_GLOBE\_R2015A\_54009\_1k_ from https://bit.ly/2lGWM5K

## Gross State Domestic Product (GSDP) &amp; Share of Agriculture in GSDP

GSDP (at Market Price) for 2015-2016 at constant 2011-2012 prices

**Sources**

For all states and territories except West Bengal, the GDP numbers were readily available at [http://mospi.gov.in/sites/default/files/press\_releases\_statements/StatewiseDomesticProduct\_28feb18.xls](http://mospi.gov.in/sites/default/files/press_releases_statements/StatewiseDomesticProduct_28feb18.xls) .

Since the Government of West Bengal hasn&#39;t released the GDP figures for 2011-2012 prices yet, a proxy was generated. Steps below:

1. West Bengal nominal GDP figures (only till 2014-2015) were retrieved from [http://niti.gov.in/content/2004-05-series](http://niti.gov.in/content/2004-05-series)
2. 2015-2016 nominal GDP figures were then estimated by taking an average growth rate of 14.41% in nominal GDP using the growth rate in previous years
3. 2015-2016 GDP at 2011-2012 prices was then estimated using the GDP deflator in [https://data.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG](https://data.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG)
4. Agriculture&#39;s share in GDP was calculated in a similar way as in 2.



## State Boundaries

[https://github.com/datameet/maps/tree/master/Districts](https://github.com/datameet/maps/tree/master/Districts)



# Methodology

The methodology draws heavily from Ghosh, T., Powell, R., Elvidge, C. D., Baugh, K. E., Sutton, P. C., &amp; Anderson, S. (2010). The basic idea can be conveyed as follows:

1. Add the light value of all pixels within each region i. This gives the sum of lights for each region (SLi)
2. Derive Ri = SLi/GSDPi where GSDPi represents the gross state domestic product for region i and Ri is a ratio that essentially tells us &#39;how much light is emitted as a proportion of the GSDP&#39; for each region i.
3. The GSDP for each pixel is finally calculated as follows:
a)Industrial and Non-Agricultural Component: Calculate how much light is emitted by that pixel relative to the total light emitted by the state – say 2%. Multiply 2% by the SGDP for the state giving SGDPa
b)Agricultural/Non-Industrial Component: Calculate how many people live in the pixel relative to the total population of the state – say 5%. Multiply 5% by the agricultural SGDP for the state giving SGDPb.
c)Add SGDPa and SGDPb


# Final Result

The final result is 1km2 grid depicting 2015-2016 GDP constant 2011-2012 prices. Each pixel expressed as INR


# Limitations

Areas with extremely bright lights get allocated commensurate GDP figures – for example visible spikes are seen in places like Jamnagar (Gujarat), Surasaniyanam (slightly East of Vijayawada in Andhra Pradesh) and in Dibrugarh (Assam). Since this is most likely caused by the prevalence of oil refineries in these areas, the allocation might not be entirely misleading. 

Since state-level GDP data is collected by the respective State Governments (and not the Union), the GDP methodology might not be standardised across the states. While this would not affect within-state comparisons of GDP, it could affect across-state comparisons.

In essence, the limitations of the methodology in Ghosh, T., Powell, R., Elvidge, C. D., Baugh, K. E., Sutton, P. C., &amp; Anderson, S. (2010) apply to this data-set as well. That leads us to the important caveat that while the original intention of the methodology was to disaggregate GDP, the dataset might work much better if looked at as a bunch of clusters rather than as a bunch of individual grids.


(Thanks to Ben Balter's sleek Word to Markdown tool on https://word-to-markdown.herokuapp.com/)
