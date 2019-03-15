#!/bin/sh
# *******************************************************************************
# * Copyright 2013, by the California Institute of Technology.
# * ALL RIGHTS RESERVED. United States Government Sponsorship
# * acknowledged. Any commercial use must be negotiated with the Office
# * of Technology Transfer at the California Institute of Technology.
# *
# * This software may be subject to U.S. export control laws and
# * regulations. By accepting this document, the user agrees to comply
# * with all applicable U.S. export laws and regulations.  User has the 
# * responsibility to obtain export licenses,
# * or other export authority as may be required before exporting such
# * information to foreign countries or providing access to foreign
# * persons.
# *
DIRNAME="`dirname $0`"
# Set BUILD_ROOT if unset or "" set the BUILD_ROOT to be the above dir
if [ -z ${BUILD_ROOT} ]
then
    export BUILD_ROOT="`cd ${DIRNAME}/../..; pwd`"
fi
echo "BUILD_ROOT is: ${BUILD_ROOT}"
# Get binary output path
export NATIVE_BUILD="`make -f ${BUILD_ROOT}/mk/makefiles/build_vars.mk print_native_build`"
echo "NATIVE_BUILD: ${NATIVE_BUILD}"
export OUTPUT_DIR="`make -f ${BUILD_ROOT}/mk/makefiles/build_vars.mk BUILD=$NATIVE_BUILD print_output_dir`"
echo "OUTPUT_DIR: ${OUTPUT_DIR}"

export PYTHONPATH="${BUILD_ROOT}/Gds"
python ${BUILD_ROOT}/Ref/scripts/run_ref_gds.py "$@" &
