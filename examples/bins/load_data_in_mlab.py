#!/usr/bin/env python3

# Copyright (C) 2021 Gabriele Bozzola
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, see <https://www.gnu.org/licenses/>.

import logging
import os

from mayavi import mlab
from numpy import log10

from kuibit.simdir import SimDir
from kuibit import argparse_helper as pah
from kuibit.grid_data_utils import load_UniformGridData

from kuibit.visualize_mayavi import (
    plot_apparent_horizon,
)

"""This script loads a grid function from a saved file and opens an interactive
mayavi session."""

if __name__ == "__main__":

    desc = __doc__

    parser = pah.init_argparse(desc)
    pah.add_figure_to_parser(parser)
    pah.add_horizon_to_parser(parser)

    parser.add_argument(
        "--datafile",
        required=True,
        help="File with the data",
    )

    parser.add_argument(
        "--vector-files",
        nargs=3,
        help="Files with the vector field data",
    )

    parser.add_argument(
        "--logscale",
        action='store_true',
        help="Take the log in base 10",
    )

    args = pah.get_args(parser)

    # Parse arguments
    logger = logging.getLogger(__name__)

    if args.verbose:
        logging.basicConfig(format="%(asctime)s - %(message)s")
        logger.setLevel(logging.DEBUG)

    logger.debug(f"Reading file {args.datafile}")
    data = load_UniformGridData(args.datafile)

    if data.num_dimensions != 3:
        raise RuntimeError("This script works only with 3D data")

    data_array = log10(data.data) if args.logscale else data.data

    mlab.contour3d(*data.coordinates_from_grid(as_same_shape=True),
                   data_array,
                   transparent=True)

    if args.vector_files:
        vec_x = load_UniformGridData(args.vector_files[0])
        vec_y = load_UniformGridData(args.vector_files[1])
        vec_z = load_UniformGridData(args.vector_files[2])

        mlab.quiver3d(*vec_x.coordinates_from_grid(as_same_shape=True),
                      vec_x.data, vec_y.data, vec_z.data)

    if (args.ah_show):
        sim = SimDir(args.datadir, ignore_symlinks=args.ignore_symlinks)
        for ah in sim.horizons.available_apparent_horizons:
            # We don't care about the QLM index here
            hor = sim.horizons[0, ah]
            logger.debug(f"Plotting apparent horizon {ah}")
            plot_apparent_horizon(hor, data.iteration)

    mlab.show()
