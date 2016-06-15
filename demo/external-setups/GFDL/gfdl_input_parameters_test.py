import getpass

# Must be set to allow correct metrics install to be picked up
buildDate = '150113'

##########################################################################
#  OPTIONS ARE SET BY USER IN THIS FILE AS INDICATED BELOW BY:
#
##########################################################################

# RUN IDENTIFICATION
# DEFINES A SUBDIRECTORY TO METRICS OUTPUT RESULTS SO MULTIPLE CASES CAN
# BE COMPARED
case_id = 'sampletest'
# LIST OF MODEL VERSIONS TO BE TESTED - WHICH ARE EXPECTED TO BE PART OF
# CLIMATOLOGY FILENAME
model_versions = ['GFDL-CM4', 'GFDL-ESM2G', ]

# VARIABLES AND OBSERVATIONS TO USE
# Variable acronyms are described in the CMIP5 standard output document
# See: http://cmip-pcmdi.llnl.gov/cmip5/docs/standard_output.pdf
vars = [
    'tos',
    'zg_500',
    'rlut',
    'rlutcs',
    'pr',
    'psl',
    'rsut',
    'rsutcs',
    'tas',
    'ta_850',
    'uas',
    'ua_200',
    'ua_850',
    'vas',
    'va_200',
    'va_850']  # Full GFDL test suite

# Observations to use "default", "alternate" or "all" or a specific obs
# reference e.g. "ref3"
# 'default' ; 'all' ; # Selecting 'default' uses a single obs dataset, 'all' processes against all available datasets
ref = 'all'
ext = '.nc'  # '.xml'

# INTERPOLATION OPTIONS
targetGrid = '2.5x2.5'  # OPTIONS: '2.5x2.5' or an actual cdms2 grid object
regrid_tool = 'esmf'  # 'regrid2' # OPTIONS: 'regrid2','esmf'
# OPTIONS: 'linear','conservative', only if tool is esmf
regrid_method = 'linear'
regrid_tool_ocn = 'esmf'    # OPTIONS: "regrid2","esmf"
# OPTIONS: 'linear','conservative', only if tool is esmf
regrid_method_ocn = 'linear'

# SIMULATION PARAMETERS
period = '01-12'
realization = 'r1i1p1'

# SAVE INTERPOLATED MODEL CLIMATOLOGIES ?
save_mod_clims = True  # True or False

# DATA LOCATION: MODELS, OBS AND METRICS OUTPUT

# Templates for climatology files
# TEMPLATE EXAMPLE: tas_GFDL-ESM2G_experiment_Amon_r1i1p1_198001-199912-clim.nc
filename_template = "%(variable)_%(model_version)_experiment_%(table)_%(realization)_%(period)-clim.nc"

# dictionary for custom %(keyword) designed by user
# Driver will match each key to its value defined by a variable name
# OR all if variable name is not present, OR "" if "all" is not defined
# custom_keys = { "key1": {"all":"key1_value_for_all_var", "tas" : "key1_value_for_tas"},
#    }

# ROOT PATH FOR MODELS CLIMATOLOGIES
mod_data_path = ''.join(
    ['/home/', getpass.getuser(), '/', buildDate, '_metrics/test/'])
# ROOT PATH FOR OBSERVATIONS
obs_data_path = ''.join(['/home/', getpass.getuser(), '/obs/'])
# DIRECTORY WHERE TO PUT RESULTS - case_id will be appended to this path
metrics_output_path = './metrics_output_path'
# DIRECTORY WHERE TO PUT INTERPOLATED MODELS' CLIMATOLOGIES - case_id will
# be appended to this path
model_clims_interpolated_output = './metrics_output_path/Interpolation_Output'
# FILENAME FOR INTERPOLATED CLIMATOLOGIES OUTPUT
filename_output_template = "%(model_version)_experiment_%(table)_%(realization)_' +\
        '%(variable)%(level)_%(period)_interpolated_%(regridMethod)_%(targetGridName)-AC%(ext)"
