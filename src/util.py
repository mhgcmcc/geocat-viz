def add_lat_lon_ticklabels(ax, zero_direction_label=False, dateline_direction_label=False):
    """
    Utility function to make plots look like NCL plots by using latitude, longitude tick labels

    Args:

        ax (:class:`matplotlib.axes._subplots.AxesSubplot` or :class:`cartopy.mpl.geoaxes.GeoAxesSubplot`):
            Current axes to the current figure

        zero_direction_label (:class:`bool`):
            Set True to get 0 E / O W or False to get 0 only.

        dateline_direction_label (:class:`bool`):
            Set True to get 180 E / 180 W or False to get 180 only.
    """
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

    lon_formatter = LongitudeFormatter(zero_direction_label=zero_direction_label,
                                       dateline_direction_label=dateline_direction_label)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)

def add_major_minor_ticks(ax, x_minor_per_major=3, y_minor_per_major=3, labelsize="small"):
    """
    Utility function to make plots look like NCL plots by adding minor and major tick lines

    Args:

        ax (:class:`matplotlib.axes._subplots.AxesSubplot` or :class:`cartopy.mpl.geoaxes.GeoAxesSubplot`):
            Current axes to the current figure

        x_minor_per_major (:class:`int`):
            Number of minor ticks between adjacent major ticks on x-axis

        y_minor_per_major (:class:`int`):
            Number of minor ticks between adjacent major ticks on y-axis
    """
    import matplotlib.ticker as tic

    ax.tick_params(labelsize=labelsize)
    ax.minorticks_on()
    ax.xaxis.set_minor_locator(tic.AutoMinorLocator(n=x_minor_per_major))
    ax.yaxis.set_minor_locator(tic.AutoMinorLocator(n=y_minor_per_major))

    # length and width are in points and may need to change depending on figure size etc.
    ax.tick_params(
        "both",
        length=8,
        width=0.9,
        which="major",
        bottom=True,
        top=True,
        left=True,
        right=True,
    )
    ax.tick_params(
        "both",
        length=4,
        width=0.4,
        which="minor",
        bottom=True,
        top=True,
        left=True,
        right=True,
    )

def set_titles_and_labels(ax, maintitle=None, maintitlefontsize=18, lefttitle=None, lefttitlefontsize=18, righttitle=None, righttitlefontsize=18,
                          xlabel=None, ylabel=None, labelfontsize=16):
    """
    Utility function to handle axis titles, left/right aligned titles, and labels as they appear in NCL plots.

    The intent of this function is to help make the plot look like an NCL plot as well as to help developers use only
    this convenience function instead of multiple matplotlib.axes.Axes functions, when applicable.

    (1) If no lefttitle and righttitle is set, maintitle is placed just top to the axes as follows:

                     maintitle
     ___________________________________________
    |                   Axes                    |
    |                                           |

    (2) If any of lefttitle or righttitle is set, lefttitle and righttitle are placed into a row that is just top to the axes, and maintitle is placed to top of
    the row of lefttitle/righttitle as follows:

                     maintitle
     lefttitle                        righttitle
     ___________________________________________
    |                   Axes                    |
    |                                           |

    Args:

        ax (:class:`matplotlib.axes._subplots.AxesSubplot` or :class:`cartopy.mpl.geoaxes.GeoAxesSubplot`):
            Current axes to the current figure

        maintitle (:class:`str`):
            Text to use for the maintitle.

        maintitlefontsize (:class:`int`):
            Text font size for maintitle. A default value of 18 is used if nothing is set.

        lefttitle (:class:`str`):
            Text to use for an optional left-aligned title, if any. For most plots, only a maintitle is enough,
            but for some plot types, a lefttitle likely with a right-aligned title, righttitle, can be used together.

        lefttitlefontsize (:class:`int`):
            Text font size for lefttitle. A default value of 18 is used if nothing is set.

        righttitle (:class:`str`):
            Text to use for an optional right-aligned title, if any. For most plots, only a maintitle is enough,
            but for some plot types, a righttitle likely with a left-aligned title, lefttitle, can be used together.

        righttitlefontsize (:class:`int`):
            Text font size for righttitle. A default value of 18 is used if nothing is set.

        xlabel (:class:`str`):
            Text for the x-axis label.

        ylabel (:class:`str`):
            Text for the y-axis label.

        labelfontsize (:class:`int`):
            Text font size for x- and y-axes. A default value of 16 is used if nothing is set.
    """

    if maintitle is not None:
        if lefttitle is not None or righttitle is not None:
            ax.set_title(maintitle, fontsize=maintitlefontsize + 2, y=1.12)
        else:
            ax.set_title(maintitle, fontsize=maintitlefontsize, y=1.04)

    if lefttitle is not None:
        ax.set_title(lefttitle, fontsize=lefttitlefontsize, y=1.04, loc='left')

    if righttitle is not None:
        ax.set_title(righttitle, fontsize=righttitlefontsize, y=1.04, loc='right')

    if xlabel is not None:
        ax.set_xlabel(xlabel, fontsize=labelfontsize)

    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize=labelfontsize)

def set_axes_limits_and_ticks(ax, xlim=None, ylim=None, xticks=None, yticks=None, xticklabels=None, yticklabels=None):
    """
    Utility function to determine axis limits, tick values and labels

    The intent of this function is to help developers use only this convenience function instead of multiple
    matplotlib.axes.Axes functions, when applicable.

    Args:

        ax (:class:`matplotlib.axes._subplots.AxesSubplot` or :class:`cartopy.mpl.geoaxes.GeoAxesSubplot`):
            Current axes to the current figure

        xlim (:class:`tuple`):
            Should be given as a tuple of numeric values (left, right), where left and right are the left and right
            x-axis limits in data coordinates. Passing None for any of them leaves the limit unchanged. See Matplotlib
            documentation for further information.

        ylim (:class:`tuple`):
            Should be given as a tuple of numeric values (left, right), where left and right are the left and right
            y-axis limits in data coordinates. Passing None for any of them leaves the limit unchanged. See Matplotlib
            documentation for further information.

        xticks (:class:`list`):
            List of x-axis tick locations. See Matplotlib documentation for further information.

        yticks (:class:`list`):
            List of y-axis tick locations. See Matplotlib documentation for further information.

        xticklabels (:class:`list[str]`):
            List of string labels for x-axis ticks. See Matplotlib documentation for further information.

        yticklabels (:class:`list[str]`):
            List of string labels for y-axis ticks. See Matplotlib documentation for further information.
    """

    if xticks is not None:
        ax.set_xticks(xticks)

    if yticks is not None:
        ax.set_yticks(yticks)

    if xticklabels is not None:
        ax.set_xticklabels(xticklabels)

    if yticklabels is not None:
        ax.set_yticklabels(yticklabels)

    if xlim is not None:
        ax.set_xlim(xlim)

    if ylim is not None:
        ax.set_ylim(ylim)

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100, name=None):
    """
    Utility function that truncates a colormap.
    Registers the new colormap by name in plt.cm, and also returns the updated map.

    Copied from  https://stackoverflow.com/questions/18926031/how-to-extract-a-subset-of-a-colormap-as-a-new-colormap-in-matplotlib

    Args:

        cmap (:class:`matplotlib.colors.Colormap`):
            Colormap to be truncated.

        minval (:class:`int` or :class:`float`):
            Minimum value to be used for truncation of the color map.

        maxval (:class:`int` or :class:`float`):
            Maximum value to be used for truncation of the color map.

        n (:class:`int`):
            Number of color values in the new color map.

        name (:class:`str`):
            Optional name of the new color map. If not set, a new name is generated by using the name of the input
            colormap as well as min and max values.
    """
    import numpy as np
    import matplotlib as mpl
    from matplotlib import cm

    if not name:
        name="trunc({n},{a:.2f},{b:.2f})".format(n=cmap.name, a=minval, b=maxval)
    new_cmap = mpl.colors.LinearSegmentedColormap.from_list(
        name=name,
        colors=cmap(np.linspace(minval, maxval, n)),
    )
    cm.register_cmap(name, new_cmap)
    return new_cmap

def xr_add_cyclic_longitudes(da, coord):
    """
    Utility function to handle the no-shown-data artifact of 0 and 360-degree longitudes

    Args:

        da (:class:`xarray.core.dataarray.DataArray`):
            Data array that contains one or more coordinates, strictly including the coordinate with the name
            given with the "coord" parameter.

        coord (:class:`str`):
            Name of the longitude coordinate within "da" data array.
    """

    import xarray as xr
    import cartopy.util as cutil

    cyclic_data, cyclic_coord = cutil.add_cyclic_point(da.values, coord=da[coord])

    coords = da.coords.to_dataset()
    coords[coord] = cyclic_coord

    new_da = xr.DataArray(cyclic_data, dims=da.dims, coords=coords.coords, attrs=da.attrs)
    new_da.encoding = da.encoding

    return new_da

def set_map_boundary(ax, lon_range, lat_range, north_pad=0, south_pad=0, east_pad=0, west_pad=0, res=1):
    """
    Utility function to set the boundary of ax to a path that surrounds a
    given region specified by latitude and longitude coordinates. This
    boundary is drawn in the projection coordinates and therefore follows
    any curves created by the projection. As of now, this only works
    consistently for the Lambert Conformal Projection and North/South
    Polar Stereographic Projections.

    Note: Due to the behavior of cartopy's set_extent() function, the curved 
    edges of the boundary may be flattened and cut off. To solve this, use the
    kwargs north_pad, south_pad, east_pad, and west_pad. These will modify the
    coordinates passed to set_extent(). For the Lambert Conformal and Polar
    Stereographic projections, typically only north_pad and south_pad are
    needed. If attempting to use this function for other projections
    (i.e. Othographic) east_pad and west_pad may be needed.

    Args:
        ax (:class:`matplotlib.axes`):
            The axes to which the boundary will be applied.

        lon_range (:class:`tuple` or :class:`list`):
            The two-tuple containing the start and end of the desired range of
            longitudes. The first entry must be smaller than the second entry,
            except when the region crosses the antimeridian. Both entries must
            be between [-180 , 180]. If lon_range is from -180 to 180, then a
            full circle centered on the pole with a radius from the pole to the
            lowest latitude given by lat_range will be set as the boundary.

        lat_range (:class:`tuple` or :class:`list`):
            The two-tuple containing the start and end of the desired range of
            latitudes. The first entry must be smaller than the second entry.
            Both entries must be between [-90 , 90].

        north_pad (:class:`int`):
            A constant to be added to the second entry in lat_range. Use this
            if the northern edge of the plot is cut off. Defaults to 0.

        south_pad (:class:`int`);
            A constant to be subtracted from the first entry in lat_range. Use
            this if the southern edge of the plot is cut off. Defaults to 0.

        east_pad (:class:`int`):
            A constant to be added to the second entry in lon_range. Use this
            if the eastern edge of the plot is cut off. Defaults to 0.
        
        west_pad (:class:`int`):
            A constant to be subtracted from the first entry in lon_range. Use
            this if the western edge of the plot is cut off. Defaults to 0.

        res (:class:`int`):
            The size of the incrementation for vertices in degrees. Default is
            a vertex every one degree of longitude. A higher number results in
            a lower resolution boundary.
    """
    import cartopy.crs as ccrs
    import matplotlib.path as mpath
    import matplotlib.patches as mpatches
    import numpy as np

    if (lon_range[0] >= lon_range[1]): 
        if not (lon_range[0] > 0 and lon_range[1] < 0):
            raise ValueError("The first longitude value must be strictly less than the second longitude value unless the region crosses over the antimeridian")

    if (lat_range[0] >= lat_range[1]):
        raise ValueError("The first latitude value must be strictly less than the second latitude value")

    if (lon_range[0] > 180 or lon_range[0] < -180 or lon_range[1] > 180 or lon_range[1] < -180):
        raise ValueError("The longitudes must be within the range [-180, 180] inclusive")

    if (lat_range[0] > 90 or lat_range[0] < -90 or lat_range[1] > 90 or lat_range[1] < -90):
        raise ValueError("The latitudes must be within the range [-90, 90] inclusive")
    

    # Make a boundary path in PlateCarree projection beginning in the south
    # west and continuing anticlockwise creating a point every `res` degree
    if (lon_range[0] >= 0 and lon_range[1] <= 0): # Case when range crosses antimeridian
        vertices = [(lon, lat_range[0]) for lon in range(lon_range[0], 180 + 1, res)] + \
                   [(lon, lat_range[0]) for lon in range(-180, lon_range[1] + 1, res)] + \
                   [(lon_range[1], lat) for lat in range(lat_range[0], lat_range[1] + 1, res)] + \
                   [(lon, lat_range[1]) for lon in range(lon_range[1], -180 - 1, -res)] + \
                   [(lon, lat_range[1]) for lon in range(180, lon_range[0] - 1, -res)] + \
                   [(lon_range[0], lat) for lat in range(lat_range[1], lat_range[0] - 1, -res)]
        path = mpath.Path(vertices)         
    elif ((lon_range[0] == 180 or lon_range[0] == -180) and (lon_range[1] == 180 or lon_range[1] == -180)):  
        vertices = [(lon, lat_range[0]) for lon in range(0, 360 + 1, res)]
        path = mpath.Path(vertices)
    else:
        vertices = [(lon, lat_range[0]) for lon in range(lon_range[0], lon_range[1] + 1, res)] + \
                   [(lon_range[1], lat) for lat in range(lat_range[0], lat_range[1] + 1, res)] + \
                   [(lon, lat_range[1]) for lon in range(lon_range[1], lon_range[0] - 1, -res)] + \
                   [(lon_range[0], lat) for lat in range(lat_range[1], lat_range[0] - 1, -res)]
        path = mpath.Path(vertices)
    

    proj_to_data = ccrs.PlateCarree()._as_mpl_transform(ax) - ax.transData
    ax.set_boundary(proj_to_data.transform_path(path))

    ax.set_extent([lon_range[0] - west_pad, lon_range[1] + east_pad,
                  lat_range[0] - south_pad, lat_range[1] + north_pad],
                  crs=ccrs.PlateCarree())

###############################################################################
#
# The following functions are deprecated and should eventually be removed 
#
###############################################################################

def nclize_axis(ax, minor_per_major=3):
    """
    Utility function to make plots look like NCL plots

    Deprecated, use `add_major_minor_ticks` instead
    """
    import warnings
    warnings.simplefilter('always', DeprecationWarning)
    warnings.warn('geocat.viz.util.nclize_axis: This function has been '
                  'deprecated, please use geocat.viz.util.add_major_minor_ticks'
                  ' instead.', DeprecationWarning, stacklevel=2)
    warnings.filters.pop(0)

    add_major_minor_ticks(ax, x_minor_per_major=minor_per_major, y_minor_per_major=minor_per_major)

def make_byr_cmap():
    """
    Define the byr colormap
    Note: this will be replaced with cmaps.BlueYellowRed
    """
    from . import cmaps

    import warnings
    warnings.simplefilter('always', DeprecationWarning)
    warnings.warn('geocat.viz.util.make_byr_cmap: This function has been '
                  'deprecated, please use geocat.viz.cmaps.BlueYellowRed '
                  'instead.', DeprecationWarning, stacklevel=2)
    warnings.filters.pop(0)

    return cmaps.BlueYellowRed
