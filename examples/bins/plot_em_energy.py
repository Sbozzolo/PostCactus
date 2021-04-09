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

import matplotlib.pyplot as plt

from kuibit.simdir import SimDir
from kuibit import argparse_helper as pah
from kuibit.visualize_matplotlib import (
    setup_matplotlib,
    save,
)

"""Plot the energy lost in electromagnetic waves (instantaneous and cumulative)."""

if __name__ == "__main__":
    setup_matplotlib()

    desc = __doc__

    parser = pah.init_argparse(desc)
    pah.add_figure_to_parser(parser)

    parser.add_argument(
        "--detector-num",
        type=int,
        required=True,
        help="Number of the spherical surface over which to read Phi2",
    )

    args = pah.get_args(parser)

    logger = logging.getLogger(__name__)

    if args.verbose:
        logging.basicConfig(format="%(asctime)s - %(message)s")
        logger.setLevel(logging.DEBUG)

    if args.figname is None:
        figname = f"em_energy_det{args.detector_num}"
    else:
        figname = args.figname

    sim = SimDir(args.datadir, ignore_symlinks=args.ignore_symlinks)

    radius = sim.electromagneticwaves.radii[args.detector_num]

    logger.debug("Computing energy")
    energy = sim.electromagneticwaves[radius].get_total_energy()
    logger.debug("Computed energy")

    logger.debug("Computing power")
    power = sim.electromagneticwaves[radius].get_total_power()
    logger.debug("Computed power")

    logger.debug("Plotting")

    fig, (ax1, ax2) = plt.subplots(2, sharex=True)

    ax1.plot(power.time_shifted(-radius))
    ax2.plot(energy.time_shifted(-radius) - energy(radius))
    ax2.set_xlabel(r"Time - Detector distance $(t - r)$")
    ax1.set_ylabel(r"$dE\slash dt (t)$")
    ax2.set_ylabel(r"$E^{<t}(t)$")

    output_path = os.path.join(args.outdir, figname)
    logger.debug(f"Saving in {output_path}")
    save(output_path, args.fig_extension, as_tikz=args.as_tikz)